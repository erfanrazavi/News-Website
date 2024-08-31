from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login , logout
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
import sweetify
from .forms import SignupForm , EmailLoginForm
from django.contrib.auth.models import User

# from .forms import CustomUserCreationForm

    

# Create your views here.
def signin_views(request):
    if request.method == "POST":
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if User.objects.filter(email=email).exists():
                user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                sweetify.success(request, 'ورود شما موفقیت آمیز بود', button='حله')
                return redirect('/')
            else:
                sweetify.error(request, 'ورود شما با خطا مواجه شد', button='حله')
        else:
            sweetify.error(request, 'فرم ارسال نشده است یا اطلاعات وارد شده صحیح نیست', button='حله')
    else:
        form = EmailLoginForm()
    
    context = {'form': form}
    return render(request, 'accounts/signin.html', context)



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