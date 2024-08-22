from django.urls import path
from index.views import *

app_name = 'index'
urlpatterns = [
    path('' , index_views , name = 'index'),
    path('about-us' , about_views , name = 'about'),
    path('contact-us' , contact_views , name = 'contact'),
    path('signin' , signin_views , name = 'signin'),
    path('signup' , signup_views , name = 'signup'),
]

