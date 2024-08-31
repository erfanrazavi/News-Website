from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=255)
    first_name = forms.CharField(max_length=255, required=False)
    last_name = forms.CharField(max_length=255 , required=False)
    email = forms.EmailField(max_length=255)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
   
    class Meta:
        model = User
        fields = ['username' ,'first_name' , 'last_name', 'email' , 'password1' , 'password2']