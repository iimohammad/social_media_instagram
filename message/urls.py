# urls.py
from rest_framework import routers
from django.urls import path, include
from .views import SendMessageAPIView, ReceiveMessageAPIView, TestMessageList, ImageMessageList, AudioMessageList

router = routers.DefaultRouter()
router.register(r'test-messages', TestMessageList, basename='test-messages')
router.register(r'image-messages', ImageMessageList, basename='image-messages')
router.register(r'audio-messages', AudioMessageList, basename='audio-messages')

urlpatterns = [
    path('', include(router.urls)),
    path('send/', SendMessageAPIView.as_view(), name='send_message'),
    path('receive/', ReceiveMessageAPIView.as_view(), name='receive_message'),
]

