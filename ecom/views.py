from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UsedPostForm,ItemForm,BusinessForm
from .models import Used,Item,Business
from django.http import HttpResponseRedirect


# Create your views here.

def home(request):
    return render(request, 'ecom/home.html')

def contact(request):
    return render(request, 'ecom/contact.html')

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
    return render(request,'ecom/orders.html')


#ECOM

def catalog(request):
    Items= Item.objects.order_by('-title')
    return render(request, 'ecom/catalog.html',{'Items':Items})

def itemdetail(request, product_id):
    product= get_object_or_404(Item,pk=product_id)
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


#REFUB

def used(request):
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

#BUSINESS

def business(request):
    products= Business.objects.order_by('-title')
    return render(request, 'ecom/business.html',{'products':products})

def businessdetail(request, product_id):
    product= get_object_or_404(Business,pk=product_id)
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
