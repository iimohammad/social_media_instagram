from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FollowViewSet, UserAccountViewSet, RegisterApi,
    PublicProfilesViewSet, FollowingProfilesViewSet, ProfileViewSet
)

# Create a router
router = routers.DefaultRouter()

# Register your viewsets with the router
router.register(r'follows', FollowViewSet, basename='follow')
router.register(r'user-accounts', UserAccountViewSet, basename='user-account')
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'public-profiles', PublicProfilesViewSet, basename='public-profile')
router.register(r'following-profiles', FollowingProfilesViewSet, basename='following-profile')


# Define additional paths if needed
urlpatterns = [
    path('register/', RegisterApi.as_view(), name='register'),
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='login'),
]

