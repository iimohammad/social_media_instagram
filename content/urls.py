from django.urls import path
from .views import PostListCreateAPIView, StoryListCreateAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list'),
    path('stories/', StoryListCreateAPIView.as_view(), name='story-list'),
]
