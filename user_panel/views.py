from http.client import METHOD_NOT_ALLOWED
from urllib import request
from django.shortcuts import redirect
from django_filters.rest_framework import DjangoFilterBackend
from django.db import IntegrityError
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import viewsets, filters, generics
from rest_framework import permissions
from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from .models import Follow, CustomUser, Profile
from .serializers import *
from .permissions import IsOwnerOrReadOnly
# Registration API


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({"error": "Please Logout First"},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        Profile.objects.create(user=user)

        token, _ = Token.objects.get_or_create(user=serializer.instance)
        return Response({"user": UserAccountSerializer(
            user, context=self.get_serializer_context()).data})


class UserAccountViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin,
                         DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = UserAccountSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter,)
    filter_fields = ('username',)

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)


class PublicProfilesViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PublicProfilesSerializer

    def get_queryset(self):
        queryset = Profile.objects.filter(is_public=True)
        return queryset


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(
            user=self.request.user.id).order_by('-pk')

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        if instance.user != request.user:
            return Response(
                {"error": "You don't have permission to update this profile."}, status=status.HTTP_403_FORBIDDEN)

        instance.bio = serializer.validated_data.get('bio', instance.bio)
        instance.profile_picture = serializer.validated_data.get(
            'profile_picture', instance.profile_picture)
        instance.is_public = serializer.validated_data.get(
            'is_public', instance.is_public)
        custom_user_data = serializer.validated_data.get('user', {})
        custom_user = instance.user
        custom_user.first_name = custom_user_data.get(
            'first_name', custom_user.first_name)
        custom_user.last_name = custom_user_data.get(
            'last_name', custom_user.last_name)
        custom_user.phone_number = custom_user_data.get(
            'phone_number', custom_user.phone_number)
        custom_user.save()
        instance.save()

        return Response(serializer.data)


class FollowingProfilesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PublicProfilesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = Follow.objects.filter(follower=self.request.user).values_list(
            'following', flat=True)        # Retrieve profiles of the following users
        return Profile.objects.filter(user__in=following_users)


class FollowingViewSet(viewsets.ModelViewSet):
    serializer_class = FollowingSerializer
    queryset = Follow.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(follower=self.request.user)


class FollowerViewSet(DestroyModelMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Follow.objects.filter(following=self.request.user)
