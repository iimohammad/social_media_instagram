# urls.py
from rest_framework import routers
from django.urls import path, include
from .views import ShowMyRecieveMessageViewSet, SendMessageViewSet

router = routers.DefaultRouter()
router.register("showReciveMessage",ShowMyRecieveMessageViewSet,basename='showReciveMessage')
router.register("SendMessage",SendMessageViewSet,basename='SendMessage')

urlpatterns = [
    path('', include(router.urls)),
]
