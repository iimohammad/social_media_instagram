from django.urls import path
from .views import CommentListCreateAPIView, LikeListCreateAPIView

urlpatterns = [
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list'),
    path('likes/', LikeListCreateAPIView.as_view(), name='like-list'),
]
