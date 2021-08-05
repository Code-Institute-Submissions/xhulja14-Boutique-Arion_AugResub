from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost


class HomeView(ListView):
    model = BlogPost
    template_name = 'blog.html'


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_details.html'
