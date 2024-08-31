from django.urls import path
from accounts.views import *

app_name = 'accounts'


urlpatterns = [
    path('signin' , signin_views , name = 'signin'),
    path('signin_email' , signin_views_email , name = 'signin_email'),
    path('signup' , signup_views , name = 'signup'),
    path('logout' , logout_views , name = 'logout'),
    
]
