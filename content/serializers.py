from rest_framework import serializers

from user_panel.models import CustomUser
from .models import Post, Story, Mention


# My Posts
from rest_framework import serializers
from .models import Post, Hashtag, PostContent


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'


class PostContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostContent
        fields = ('typeContent', 'file')


class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.none())
    hashtags = HashtagSerializer(many=True)
    content = PostContentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'caption', 'user', 'hashtags', 'content')

    def create(self, validated_data):
        content_data = validated_data.pop('content')
        hashtags_data = validated_data.pop('hashtags')
        post = Post.objects.create(**validated_data)
        for content_item in content_data:
            PostContent.objects.create(post=post, **content_item)
        post.hashtags.set(hashtags_data)
        return post

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = self.get_queryset()

    def get_queryset(self):
        # Retrieve the current user from the context
        user = self.context['request'].user
        return CustomUser.objects.filter(id=user.id)


class FollowingPostSerializer(serializers.ModelSerializer):
    hashtags = HashtagSerializer(many=True, read_only=True)
    content = PostContentSerializer(many=True)
    like_count = serializers.SerializerMethodField()
    dislike_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'caption', 'user', 'hashtags',
                  'content', 'like_count', 'dislike_count')

    def get_like_count(self, obj):
        return obj.like_count()

    def get_dislike_count(self, obj):
        return obj.dislike_count()

    def create(self, validated_data):
        content_data = validated_data.pop('content')
        hashtags_data = validated_data.pop('hashtags')
        post = Post.objects.create(**validated_data)
        for content_item in content_data:
            PostContent.objects.create(post=post, **content_item)
        post.hashtags.set(hashtags_data)
        return post


class StorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.none())

    class Meta:
        model = Story
        fields = ['id', 'user', 'file']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = self.get_queryset()

    def get_queryset(self):
        # Retrieve the current user from the context
        user = self.context['request'].user
        return CustomUser.objects.filter(id=user.id)


class MentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mention
        fields = ['id', 'post', 'user']
