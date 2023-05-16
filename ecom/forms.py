from django.forms import ModelForm
from .models import Used,Item,Business,Orders


class UsedPostForm(ModelForm):
    class Meta:
        model= Used
        exclude=["user"]

class ItemForm(ModelForm):
    class Meta:
        model=Item
        exclude=["user"]

class BusinessForm(ModelForm):
    class Meta:
        model=Business
        exclude=["user"]
   
class OrderForm(ModelForm):
    class Meta:
        model=Orders
        fields= ['status']
       
