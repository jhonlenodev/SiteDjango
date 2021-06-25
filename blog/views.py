from blog.models import Post
from django.shortcuts import render
from blog.models import Post

def postsviews(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})

def postview(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'pages.html', {'post':post})