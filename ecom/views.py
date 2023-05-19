from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UsedPostForm,ItemForm,BusinessForm,OrderForm
from .models import Used,Item,Business,Category,Cart,Orders
from django.http import HttpResponseRedirect
from django.utils import timezone


# Create your views here.

def home(request):
    Items= Item.objects.order_by('-title')[:4]
    Useds=Used.get_all_useds_by_district("Jaipur")[:4]
    Products= Business.objects.order_by('-title')[:4]
    return render(request, 'ecom/home.html',{'Items':Items,'Useds':Useds,'Products':Products})

def signupuser(request):
    if request.method=='GET':
        return render(request, 'ecom/signupuser.html', {'form': UserCreationForm()})
    else:
        # Create a new user
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect(home)
            except IntegrityError:
                return render(request, 'ecom/signupuser.html', {'form': UserCreationForm(), 'error':"Username already taken"})

        else:
            return render(request, 'ecom/signupuser.html', {'form': UserCreationForm(), 'error':"Passwords didn't match"})

def loginuser(request):
    if request.method=='GET':
        return render(request, 'ecom/loginuser.html', {'form': AuthenticationForm()})
    else:
        user=authenticate(request, username=request.POST['username'] ,password=request.POST['password'])
        if user is None:
            return render(request, 'ecom/loginuser.html', {'form': AuthenticationForm(),'error':"Passwords didn't match"})
        else:
            login(request, user)
            return redirect(home)
        
@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect(home)
    
@login_required
def orders(request):

    if request.user.username=="admin":
        admin=True
        orders=Orders.objects.order_by('-timeplaced')
    else:
        admin=False
        user=request.user
        orders=Orders.get_by_user(user).order_by('-timeplaced')
        
    return render(request,'ecom/orders.html',{'orders':orders,'admin':admin})

@login_required
def orderdetail(request,order_id):
    order=get_object_or_404(Orders, pk=order_id)

    if request.method=="GET":
        if(request.user.username=="admin"):
            admin=True
        else:
            admin=False
        form=OrderForm(instance=order)
        discount=order.price-order.dprice
        return render(request,'ecom/orderdetail.html',{'order':order,'form':form,'discount':discount,'admin':admin})
    else:
        form=OrderForm(request.POST, instance=order)
        form.save()
        return redirect(orders)


@login_required
def cart(request):
    accountuser=request.user
    products=Cart.get_all_by_user(accountuser)
    total=0
    dtotal=0
    for p in products:
        total+=p.price
        dtotal+=p.dprice
    return render(request,'ecom/cart.html',{'products':products,'total':total,'dtotal':dtotal})

@login_required
def deletecart(request, cart_pk):
    product= get_object_or_404(Cart, pk=cart_pk, user=request.user)
    if request.method=='POST':
        product.delete()
        return redirect(cart)

@login_required
def checkout(request):
    accountuser=request.user
    products=Cart.get_all_by_user(accountuser)
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        for product in products:
            order=Orders()
            order.user=request.user
            order.name=name
            order.phone=phone
            order.title=product.title
            order.price=product.price
            order.dprice=product.dprice
            order.description_short=product.description_short
            order.address=address
            order.city=city
            order.pincode=pincode
            order.state=state
            order.image=product.image
            order.timeplaced=timezone.now()
            order.status="Placed"
            order.save()
            product.delete()
        return redirect(orderplaced)
    else:    
        total=0
        dtotal=0
        for p in products:
            total+=p.price
            dtotal+=p.dprice
        discount=total-dtotal
        return render(request,'ecom/checkout.html',{'products':products,'total':total,'dtotal':dtotal,'discount':discount})
    
def orderplaced(request):
    return render(request,'ecom/orderplaced.html')



#--------------------------ECOM-----------------------------

def catalog(request):
    if request.user.username == "admin":
        admin=True
    else:
        admin=False
    distval=request.GET.get('dist')
    catval=request.GET.get('cat')
    Items= None
    if distval:
        Items=Item.get_all_items_by_district(distval)
    else:
        Items= Item.objects.order_by('-title')
        if catval:
            Items=Item.get_all_items_by_category(catval)
        else:
            Items= Item.objects.order_by('-title') 
    category=Category.get_all_category()
    return render(request, 'ecom/catalog.html',{'Items':Items,'admin':admin,'categories':category})

def itemdetail(request, item_id):
    product= get_object_or_404(Item,pk=item_id)
    if request.method=='POST':
        cart=Cart()
        cart.user=request.user
        cart.title=product.title
        cart.price=product.price
        cart.dprice=product.disc_price
        cart.description_short=product.description_short
        cart.state=product.state
        cart.district=product.district
        cart.image=product.image
        cart.save()
        
    return render(request, 'ecom/itemdetail.html', {'item':product})

@login_required
def itempost(request):
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES)
        if form.is_valid():
            newused=form.save(commit=False)
            newused.user=request.user
            newused.save()
            return HttpResponseRedirect('/catalog/')
    else:
        form = ItemForm()

    return render(request, 'ecom/itempost.html', {'form': form})


#-----------------------REFUB----------------------

def used(request):
    distval=request.GET.get('dist')
    
    useds= None
    if distval:
        useds=Used.get_all_useds_by_district(distval)
    else:
        useds= Used.objects.order_by('-posted')
    return render(request, 'ecom/used.html',{'useds':useds})

@login_required
def usedpost(request):
    if request.method == 'POST':
        form = UsedPostForm(request.POST,request.FILES)
        if form.is_valid():
            newused=form.save(commit=False)
            newused.user=request.user
            newused.save()
            return HttpResponseRedirect('/used/')
    else:
        form = UsedPostForm()

    return render(request, 'ecom/usedpost.html', {'form': form})

def useddetail(request, used_id):
    uproduct= get_object_or_404(Used,pk=used_id)
    return render(request, 'ecom/useddetail.html', {'used':uproduct})

#-------------------------BUSINESS--------------------------

def business(request):
    if request.user.username == "admin":
        admin=True
    else:
        admin=False
    catval=request.GET.get('cat')
    distval=request.GET.get('dist')
    
    products= None
    
    if distval:
        products=Business.get_all_business_by_district(distval)
    else:
        products= Business.objects.order_by('-title')
        if catval:
            products=Business.get_all_business_by_category(catval)
        else:
            products= Business.objects.order_by('-title')
    categories=Category.get_all_category()
    return render(request, 'ecom/business.html',{'products':products,'admin':admin,'categories':categories})

def businessdetail(request, product_id):
    product= get_object_or_404(Business,pk=product_id)
    if request.method=='POST':
        cart=Cart()
        cart.user=request.user
        cart.title=product.title
        cart.price=product.price
        cart.dprice=product.disc_price
        cart.description_short=product.description_short
        cart.state=product.state
        cart.district=product.district
        cart.image=product.image
        cart.save()
        
    return render(request, 'ecom/businessdetail.html', {'product':product})

@login_required
def businesspost(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            newused=form.save(commit=False)
            newused.user=request.user
            newused.save()
            return HttpResponseRedirect('/business/')
    else:
        form = BusinessForm()

    return render(request, 'ecom/businesspost.html', {'form': form})
