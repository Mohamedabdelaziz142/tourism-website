from typing import Any
from django.db.models import Q, Count
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Category, Post
from taggit.models import Tag
# Create your views here.
class PostList(ListView):
    model = Post
    paginate_by = 3
       
    def get_queryset(self):
        name = self.request.GET.get('q','')
        object_list = Post.objects.filter(
            Q(title__icontains=name)|
            Q(description__icontains=name)
        )
        return object_list

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(post_count=Count('post_category'))
        context["tags"] = Tag.objects.all()
        context["recent_posts"] = Post.objects.all()[:3]
        return context
    
class PostByCategory(ListView):
    model = Post
    
    def get_queryset(self):
        slug = self.kwargs['slug']
        object_list = Post.objects.filter(
            Q(category__name__icontains = slug)
        )
        return object_list


class PostByTags(ListView):
    model = Post
    
    def get_queryset(self):
        slug = self.kwargs['slug']
        object_list = Post.objects.filter(
            Q(tags__name__icontains = slug)
        )
        return object_list
