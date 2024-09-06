from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=254)
   
   
    def __str__(self) :
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts' ,  default=1)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='images/' , null= True , blank=True)
    status = models.BooleanField(default=False)
    tags = TaggableManager()
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self) :
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:blog-single", kwargs={"pid": self.id})
     
    