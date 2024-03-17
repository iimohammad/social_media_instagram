from rest_framework import serializers
from .models import Post, Content, Story, Mention, Hashtag, ContentImage

class ContentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentImage
        fields = ['id', 'image']


class ContentSerializer(serializers.ModelSerializer):
    images = ContentImageSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        fields = ['id', 'images']


class PostSerializer(serializers.ModelSerializer):
    content_objects = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'caption', 'user', 'content_objects']


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'user']


class MentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mention
        fields = ['id', 'post', 'user']


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['id', 'post', 'title']
