from django.shortcuts import render
from .models import orders
# Create your views here.
def contact(request):
    return render(request,'Contact.html')

def PayList(request):
    
    if request.method == 'POST': 
        
         fullname =request.POST['fullname']
         email = request.POST['email']
         phonenumber = request.POST['phonenumber']
         password= request.POST['password']
         location = request.POST['location']      
         orderdetails= request.POST['orderdetails']
         
         
         
         Payment=orders(fullname=fullname,email=email,phonenumber=phonenumber,password=password,location=location,orderdetails=orderdetails,)
         Payment.save()
    return render(request,'checkout.html', {})




def check(request):
    data=orders.objects.all()
    items ={
        'data':data
    }
    return render(request,'check.html',context=items)