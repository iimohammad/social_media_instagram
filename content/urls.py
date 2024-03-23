from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MyPostViewSet,FollowingPostViewSet
)


router = DefaultRouter()
router.register(r'myposts', MyPostViewSet, basename='myposts')
router.register(r'FollowingPosts', FollowingPostViewSet, basename='FollowingPosts')
# router.register(r'mentions', MentionViewSet, basename='mentions')
# router.register(r'following/posts', FollowingPostViewSet, basename='following-posts')
# router.register(r'following/stories', FollowingStoryViewSet, basename='following-stories')

urlpatterns = [
    path('', include(router.urls)),
]
