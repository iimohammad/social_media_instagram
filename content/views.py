from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, permissions
from .models import Post, Story, Mention, Hashtag
from .serializers import PostSerializer, MentionSerializer, HashtagSerializer, StorySerializer


class BasePostRelatedViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)

    def perform_create(self, serializer):
        post_id = self.request.data.get('post', None)
        post = get_object_or_404(Post, id=post_id, user=self.request.user)
        serializer.save(post=post)


class BaseStoryRelatedViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)

    def perform_create(self, serializer):
        story_id = self.request.data.get('story', None)
        story = get_object_or_404(Story, id=story_id, user=self.request.user)
        serializer.save(story=story)


class PostViewSet(BasePostRelatedViewSet):
    serializer_class = PostSerializer
    filterset_fields = ('user',)
    search_fields = ('caption',)

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user).order_by('-pk')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        post = self.get_object()
        return response


class StoryViewSet(BaseStoryRelatedViewSet):
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Story.objects.all()

    def get_queryset(self):
        return Story.objects.filter(user=self.request.user).order_by('-pk')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class MentionViewSet(BasePostRelatedViewSet):
    serializer_class = MentionSerializer
    filterset_fields = ('post', 'user')

    def get_queryset(self):
        return Mention.objects.filter(post__user=self.request.user).order_by('-pk')


class HashtagViewSet(BasePostRelatedViewSet):
    serializer_class = HashtagSerializer
    filterset_fields = ('post', 'title')

    def get_queryset(self):
        return Hashtag.objects.filter(post__user=self.request.user).order_by('-pk')


class FollowingPostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('user',)
    search_fields = ('caption',)

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all().values_list('following', flat=True)
        return Post.objects.filter(user__in=following_users).order_by('-pk')


class FollowingStoryViewSet(BaseStoryRelatedViewSet):
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    filterset_fields = ('user',)

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all().values_list('following', flat=True)
        return Story.objects.filter(user__in=following_users).order_by('-pk')
