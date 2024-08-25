from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login , logout
from django.urls import reverse

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
    return render(request ,'accounts/signup.html')

def logout_views(request):
    logout(request)
    return redirect('/')