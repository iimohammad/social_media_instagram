from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, PostLikeViewSet, StoryLikeViewSet

# Create a router object
router = DefaultRouter()

router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'post-likes', PostLikeViewSet, basename='post-like')
router.register(r'story-likes', StoryLikeViewSet, basename='story-like')

# Define the URL patterns
urlpatterns = [
    path('', include(router.urls)),
]
