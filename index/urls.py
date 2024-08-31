from django.urls import path
from index.views import *

app_name = 'index'
urlpatterns = [
    path('' , index_views , name = 'index'),
    path('about-us' , about_views , name = 'about'),
    path('contact-us' , contact_views , name = 'contact'),
    
]

