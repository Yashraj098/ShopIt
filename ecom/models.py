from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

#Used Products
class Used(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media/used/', null=True, blank=True)
    price=models.IntegerField()
    description=models.TextField(blank=True)
    contact=PhoneField(blank=True)
    state=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    posted=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey( User ,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#New Products
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    disc_price = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=20)
    qty = models.IntegerField()
    description_short = models.CharField(max_length=50)
    description_long = models.TextField()
    image = models.ImageField(upload_to='media/Items/', null=True, blank=True)
    state=models.CharField(max_length=20,default="")
    district=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.title
    
#Business Products

class Business(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    disc_price = models.FloatField(blank=True, null=True)
    lot_size=models.IntegerField()
    min_lot=models.IntegerField()
    gst_req=models.BooleanField(default=False)
    category = models.CharField(max_length=20)
    qty = models.IntegerField()
    contact=PhoneField()
    description_short = models.CharField(max_length=50)
    description_long = models.TextField()
    image = models.ImageField(upload_to='media/business/', null=True, blank=True)
    state=models.CharField(max_length=20,default="")
    district=models.CharField(max_length=20,default="")

    def __str__(self):
        return self.title