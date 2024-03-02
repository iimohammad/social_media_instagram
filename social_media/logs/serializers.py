from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ContentLog, ProfileLog
from content.serializers import PostSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class ContentLogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = ContentLog
        fields = '__all__'

class ProfileLogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    viewed_profile = UserSerializer(read_only=True)

    class Meta:
        model = ProfileLog
        fields = '__all__'
