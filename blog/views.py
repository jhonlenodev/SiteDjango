from blog.models import Post
from django.shortcuts import render
from blog.models import Post

def postsviews(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})
