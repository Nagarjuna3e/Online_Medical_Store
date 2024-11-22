"""Pharmacy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Products.views import products
from home.views import home
from Contact.views import contact,PayList,check
from home.views import RegisList,pro
from home.views import login
from home.views import success
from home.views import about,out




urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/',products),
    path('',home),
    path('Contact/',contact),
    path('register/',RegisList),
    path('Login/',login),
    path('SignIn/',products),
    path('Submit/',success),
    path('ReturntoHome/',home),
    path('success/',success),
    path('about/',about),
    path('users/',pro), 
    path('checkout/',out),
    path('pay/',PayList),
    path('check/',check),
   
    
]
