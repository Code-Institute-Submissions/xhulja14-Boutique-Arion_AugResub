from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogPost
from .forms import PostForm

# Create your views here.


class BlogView(ListView):
    model = BlogPost
    template_name = 'blog.html' 

    BlogPost = get_object_or_404


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_details.html'

    BlogPost = get_object_or_404


class AddPostView(CreateView):
    model = BlogPost
    form_class = PostForm
    template_name = 'add_post.html'

    BlogPost = get_object_or_404
    # fields = '__all__'
