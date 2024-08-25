from django.shortcuts import render ,redirect
from blog.models import Post
from index.forms import ContactForm
from django.contrib import messages
from django.urls import reverse
import sweetify
from django.contrib.auth import authenticate, login , logout



# Create your views here.
def index_views(request):
    posts = Post.objects.filter(status=True)
    
    context = {'posts':posts}
    return render(request ,'website/index.html' , context)

def about_views(request):
    return render(request ,'website/about-us.html')

def contact_views(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            human = True

            sweetify.success(request, 'پیام شما با موفقیت ارسال شد', button='باشه')
            return redirect(reverse('index:contact'))
        else:
            # فرم نامعتبر است، بنابراین پیغام خطا را به قالب ارسال کنید
            sweetify.error(request, 'پیام شما ارسال نشد. دوباره امتحان کنید.', button='باشه')

    else:
        form = ContactForm()
        
    context = {'form': form}
    return render(request, 'website/contact-us.html', context)


def signin_views(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('/')
        else:
            redirect(reverse('index:signin'))
    
    return render(request ,'website/signin.html')

def signup_views(request):
    return render(request ,'website/signup.html')

def logout_views(request):
    logout(request)
    return redirect('/')