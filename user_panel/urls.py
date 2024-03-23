from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserAccountViewSet, RegisterApi,
    PublicProfilesViewSet, FollowingProfilesViewSet, ProfileViewSet, FollowingViewSet, FollowerViewSet
)

router = routers.DefaultRouter()
# Edit Profile
router.register(r'EditProfile', ProfileViewSet, basename='EditProfile')
# Public Profile
router.register(r'public-profiles', PublicProfilesViewSet,
                basename='public-profile')
# Show following and can add or remove
router.register('followings', FollowingViewSet, basename='followings')
# Show followers and can Delete
router.register('followers', FollowerViewSet, basename='followers')

router.register(r'following-profiles', FollowingProfilesViewSet,
                basename='following-profile')


# Define additional paths if needed
urlpatterns = [
    path('register/', RegisterApi.as_view(), name='register'),
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='login'),
]
