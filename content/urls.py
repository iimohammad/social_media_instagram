from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CreatePostAPIView,
    FollowingStoryViewSet,
    MentionViewSet,
    MyPostViewSet,
    FollowingPostViewSet,
    MyStoryViewSet,
)


router = DefaultRouter()
# Show User Posts
router.register(r'myposts', MyPostViewSet, basename='myposts')
# Show Following Posts and Can Like or Dislike
router.register(r'Following/Posts', FollowingPostViewSet,
                basename='FollowingPosts')
# Show User Story
router.register(r'Story/MyStory', MyStoryViewSet, basename='MyStory')
# Show Following Stories
router.register(r'Story/FollowingStory', FollowingStoryViewSet,
                basename='FollowingStory')
# CRUD Mention
router.register(r'mentions', MentionViewSet, basename='mentions')

urlpatterns = [
    path('', include(router.urls)),
    path('create_post/', CreatePostAPIView.as_view(), name='create_post'),
]
