from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FollowingCommentViewSet, LikeFollowingPostViewSet, MyCommentViewSet

# Create a router object
router = DefaultRouter()


router.register(r'Posts/Reactions', LikeFollowingPostViewSet,
                basename='post-like')
router.register(r'myposts/comments', MyCommentViewSet,
                basename='mypost_comments')
router.register(r'following/posts/comments',
                FollowingCommentViewSet, basename='following_posts_comments')
# Define the URL patterns
urlpatterns = [
    path('', include(router.urls)),
]
