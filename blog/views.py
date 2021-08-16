from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import BlogPost
from .forms import PostForm

# Create your views here.


class BlogView(ListView):
    model = BlogPost
    template_name = 'blog.html'


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_details.html'



class AddPostView(CreateView):
    model = BlogPost
    form_class = PostForm
    template_name = 'add_post.html'


    # fields = '__all__'


class UpdatePostView(UpdateView):
    model = BlogPost
    template_name = 'update_post.html'
    fields = ['title', 'body']

    
