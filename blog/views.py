from django.shortcuts import render , get_object_or_404
from blog.models import Post

# Create your views here.
def blog_home_views(request):
    posts = Post.objects.filter(status = True)
    
    context = {'posts' : posts }
    return render(request , 'blog/post-list.html' , context)

def blog_single_views(request , pid):
    posts = get_object_or_404(Post , id=pid)
    posts.counted_views += 1
    posts.save()
    context = {'posts' : posts }
    return render(request , 'blog/post-single.html' , context)