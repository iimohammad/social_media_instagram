from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViewLogViewSet

router = DefaultRouter()
router.register(r'view-logs', ViewLogViewSet, basename='view-logs')

urlpatterns = [
    path('', include(router.urls)),
]
