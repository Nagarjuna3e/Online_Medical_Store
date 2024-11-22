from django.db import models
from datetime import datetime

# Create your models here.
class List(models.Model):
    MedicineName = models.CharField(max_length=250)
    MedicinePrice = models.CharField(max_length=250)
    ExpiredDate = models.DateTimeField()
   
    def __str__(self):
        return self.MedicineName
    
    
        

        
     
    
