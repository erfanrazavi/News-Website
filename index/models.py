from django.db import models
# from django.contrib.auth.models import 
# Create your models here.


    
    
class Contact(models.Model):
    
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    messages = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)  
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return  self.fullname
    
    
