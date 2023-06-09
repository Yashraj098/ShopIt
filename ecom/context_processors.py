from .models import Cart

def cart_count(request):
    accountuser = request.user
    products = Cart.get_all_by_user(accountuser)
    count = products.count()
    return {'cart_count': count}