from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
# Create a router and register viewsets
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'stories', StoryViewSet, basename='stories')
router.register(r'mentions', MentionViewSet, basename='mentions')
router.register(r'following/posts', FollowingPostViewSet, basename='following-posts')
router.register(r'following/stories', FollowingStoryViewSet, basename='following-stories')

urlpatterns = [
    path('', include(router.urls)),
]
