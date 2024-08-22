from django.urls import path
from blog.views import *

app_name = 'blog'
urlpatterns = [
    path('' , blog_home_views , name = 'blog-home'),
    path('post/<int:pid>/' , blog_single_views , name = 'blog-single')
]
