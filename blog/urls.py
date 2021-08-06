from django.urls import path
from .views import HomeView, BlogDetailView, AddPostView


urlpatterns = [
    path('', HomeView.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
]
