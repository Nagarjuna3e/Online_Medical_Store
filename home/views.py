from django.shortcuts import render
from .models import Regis

# Create your views here.
def home(request):
    return render(request,'Home.html')
 
def RegisList(request):
    if request.method == 'POST':
         fullname =request.POST['name']
         email = request.POST['email']
         password= request.POST['password']
         phonenumber = request.POST['phone']
          
         Register=Regis(fullname=fullname,email=email,password=password,phonenumber=phonenumber)
         Register.save() 
    return render(request,'register.html', {})

def pro(request):
    data=Regis.objects.all()
    items ={
        'data':data
    }
    return render(request,'users.html',context=items)


def login(request):
    return render(request,'login.html')

def success(request):
    return render(request,'success.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def out(request):
    return render(request,'checkout.html')



