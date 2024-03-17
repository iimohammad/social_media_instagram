# urls.py
from rest_framework import routers
from django.urls import path, include
from .views import SendMessageAPIView, ReceiveMessageAPIView, TestMessageViewSet, ImageMessageViewSet, AudioMessageViewSet

router = routers.DefaultRouter()
router.register(r'test-messages', TestMessageViewSet, basename='test-messages')
router.register(r'image-messages', ImageMessageViewSet, basename='image-messages')
router.register(r'audio-messages', AudioMessageViewSet, basename='audio-messages')

urlpatterns = [
    path('', include(router.urls)),
    path('send/', SendMessageAPIView.as_view(), name='send_message'),
    path('receive/', ReceiveMessageAPIView.as_view(), name='receive_message'),
]
