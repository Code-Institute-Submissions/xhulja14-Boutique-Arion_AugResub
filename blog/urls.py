from django.urls import path
from .views import BlogView, BlogDetailView, AddPostView


urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
]
