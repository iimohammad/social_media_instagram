from django.urls import path
from .views import ContentLogListCreateAPIView, ProfileLogListCreateAPIView

urlpatterns = [
    path('content-logs/', ContentLogListCreateAPIView.as_view(), name='content-log-list'),
    path('profile-logs/', ProfileLogListCreateAPIView.as_view(), name='profile-log-list'),
]
