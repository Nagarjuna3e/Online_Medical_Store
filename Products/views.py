from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import List

# Create your views here.
def products(request):
    data=List.objects.all()
    items ={
        'data':data
    }
    return render(request,'Products.html',context=items)






