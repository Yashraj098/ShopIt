from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

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