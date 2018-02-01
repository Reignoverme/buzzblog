from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post
import markdown


class IndexView(ListView):
    model = Post
    template_name = 'testblog/index.html'
    context_object_name = 'posts'

# def home(request):
#     posts = Post.objects.all()

#     return render(request, 'testblog/index.html', context={
#         'posts': posts
#     })


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


def archive(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 15)
    page = request.GET.get('page')
    total_num = paginator.num_pages
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'testblog/archive.html',
                  {'posts': posts, 'page': page,
                   'total_num': total_num})
