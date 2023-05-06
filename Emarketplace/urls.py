"""Emarketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecom import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact,name='contact'),
    #Auth
    path('signup/',views.signupuser,name='signupuser'),
    path('login/',views.loginuser, name='loginuser'),
    path('logout/',views.logoutuser, name='logoutuser'),

    #ECOM
    path('',views.home, name='home'),
    path('catalog/',views.catalog,name='catalog'),
    path('orders/',views.orders,name='orders'),
    path('catalog/<int:item_id>/', views.itemdetail, name='itemdetail'),
    #REFUB
    path('used/',views.used,name='used'),
    path('used/post/',views.usedpost,name='usedpost'),
    path('used/<int:used_id>/', views.useddetail, name='useddetail'),
    #Business
    path('business/',views.business,name='business'),
    path('business/<int:product_id>/', views.businessdetail, name='businessdetail'),
    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
