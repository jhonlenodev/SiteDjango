from collections import namedtuple
from django.shortcuts import render
from blog.models import Post
from django.contrib.auth.models import User
from blog.forms import PostForm


def postsviews(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})

def postview(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'pages.html', {'post':post})

def perfilview(request, user_id):
    usuario = User.objects.get(pk=user_id)
    return render(request, 'profile.html', {'user':usuario})

def formulario(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'formulario.html', {'forms':form})
