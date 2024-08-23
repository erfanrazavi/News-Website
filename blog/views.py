from django.shortcuts import render , get_object_or_404
from blog.models import Post ,Category

# Create your views here.
def blog_home_views(request,**kwargs):
    posts = Post.objects.filter(status=1)
    
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    
    context = {'posts' : posts }
    return render(request , 'blog/post-list.html' , context)

def blog_single_views(request ,**kwargs):
    if 'pid' in kwargs:
        
        posts = get_object_or_404(Post, id=kwargs['pid'])
    else:
        
        posts = Post.objects.filter(status=True)
        if 'tag_name' in kwargs:
            posts = posts.filter(tags__name__in=[kwargs['tag_name']])
        context = {'posts': posts}
        return render(request, 'blog/post-list.html', context)
    posts.counted_views += 1
    posts.save()
    context = {'posts' : posts }
    return render(request , 'blog/post-single.html' , context)

