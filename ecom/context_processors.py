from .models import Cart
from django.contrib.auth.models import User

def cart_count(request):
    if request.user.isauthencated:
        accountuser = request.user
        products = Cart.get_all_by_user(accountuser)
        count = products.count()
        return {'cart_count': count}
    else:
        return {'cart_count': 0}