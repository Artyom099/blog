from django.shortcuts import render, get_object_or_404
from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectDetailMixin

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'app1/index.html', context={'posts': posts})

# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'app1/post_detail.html', context={'post': post})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'app1/tags_list.html', context={'tags': tags})

# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'app1/tag_detail.html', context={'tag': tag})

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'app1/post_detail.html'

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'app1/tag_detail.html'
