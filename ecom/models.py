from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField


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
    
    @staticmethod
    def get_all_useds():
        return Used.objects.all()
    @staticmethod
    def get_all_useds_by_district(dist):
        if(dist):
            return Used.objects.filter(district=dist)
        else:
            return Used.get_all_useds()

#Category List
class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.category
    @staticmethod
    def get_all_category():
        return Category.objects.all()


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
    user=models.ForeignKey( User ,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

    @staticmethod
    def get_all_items():
        return Item.objects.all()
    @staticmethod
    def get_all_items_by_district(dist):
        if(dist):
            return Item.objects.filter(district=dist)
        else:
            return Item.get_all_business()
        
    @staticmethod
    def get_all_items_by_category(cat):
        if(cat):
            return Item.objects.filter(category=cat)
        else:
            return Item.get_all_business()
    
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
    user=models.ForeignKey( User ,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    @staticmethod
    def get_all_business():
        return Business.objects.all()
    @staticmethod
    def get_all_business_by_district(dist):
        if(dist):
            return Business.objects.filter(district=dist)
        else:
            return Business.get_all_business()
        
    @staticmethod
    def get_all_business_by_category(cat):
        if(cat):
            return Business.objects.filter(category=cat)
        else:
            return Business.get_all_business()