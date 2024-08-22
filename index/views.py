from django.shortcuts import render

# Create your views here.
def index_views(request):
    return render(request ,'website/index.html')

def about_views(request):
    return render(request ,'website/about-us.html')

def contact_views(request):
    return render(request ,'website/contact-us.html')

def signin_views(request):
    return render(request ,'website/signin.html')

def signup_views(request):
    return render(request ,'website/signup.html')