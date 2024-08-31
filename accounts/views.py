from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login , logout
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
import sweetify
from .forms import SignupForm

# from .forms import CustomUserCreationForm

    

# Create your views here.
def signin_views(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('/')
        else:
            redirect(reverse('accounts:signin'))
    
    
    
        
    
    return render(request ,'accounts/signin.html')

def signup_views(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'پیام شما با موفقیت ارسال شد', button='حله')
            return redirect(reverse('accounts:signin'))
        else:
            sweetify.error(request, 'پیام شما با خطا مواجه شد', button='حله')

    form = SignupForm() 
        
    
    context = {'form' : form}        
    return render(request ,'accounts/signup.html' , context)

def logout_views(request):

    logout(request)
    return redirect('/')