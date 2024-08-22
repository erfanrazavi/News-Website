from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts' ,  default=1)
    # category
    image = models.ImageField(upload_to='images/' , null= True , blank=True)
    status = models.BooleanField(default=False)
    # tag
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self) :
        return self.title