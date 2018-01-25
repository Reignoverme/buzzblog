from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
import markdown


def home(request):
    posts = Post.objects.all()

    return render(request, 'testblog/index.html', context={
        'posts': posts
    })


def read(request, title):
    post = get_object_or_404(Post, title=title)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc', ])

    return render(request, 'testblog/post.html', context={
        'post': post
    })
