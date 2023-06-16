from django.db import models

# Create your models here.

class mode(models.Model): 
    name= models.CharField(max_length=25)
    s_email= models.EmailField()
    designation=models.CharField(max_length=10)
    phone=models.IntegerField()
    
    