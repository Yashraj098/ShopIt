from django.contrib import admin
from .models import Used,Item,Business
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class UsedAdmin(admin.ModelAdmin):
    readonly_fields=('posted',)

admin.site.register(Used)
admin.site.register(Item)
admin.site.register(Business)
