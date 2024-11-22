from django.db import models

# Create your models here.
class Regis(models.Model):
     
    fullname = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=250)
    phonenumber = models.CharField(max_length=250)
    
    
    def __str__(self): 
        return self.fullname 