from rest_framework import generics
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user.profile
