from django.urls import path
from .views import (BlogView, BlogDetailView, AddPostView,
                    UpdatePostView, DeletePostView)


urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('blog/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('blog/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
]
