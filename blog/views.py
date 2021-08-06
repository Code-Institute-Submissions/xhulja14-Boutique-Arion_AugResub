from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogPost


class HomeView(ListView):
    model = BlogPost
    template_name = 'blog.html'


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_details.html'


class AddPostView(CreateView):
    model = BlogPost
    template_name = 'add_post.html'
    fields = '__all__'
