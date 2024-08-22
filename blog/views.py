from django.shortcuts import render

# Create your views here.
def blog_home_views(request):
    return render(request , 'blog/post-list.html')