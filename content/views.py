from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, permissions, status
from rest_framework.decorators import action
from user_panel.models import Follow
from .models import Post, Reaction, Story, Mention
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


class MyPostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)




class AddContentToPost(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostContentSerializer
    def get_queryset(self):
        # Retrieve the posts belonging to the request user
        posts = Post.objects.filter(user=self.request.user)
        # Get the associated post content objects
        post_content = PostContent.objects.filter(post__in=posts)
        return post_content

    def get_serializer_context(self):
        # Include the request object in the serializer context
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

class FollowingPostViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowingPostSerializer

    def get_queryset(self):
        following_users = Follow.objects.filter(
            follower=self.request.user).values_list('following', flat=True)
        queryset = Post.objects.filter(user__in=following_users)
        return queryset

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        reaction, created = Reaction.objects.get_or_create(
            user=request.user, post=post)
        if not created:
            # Reaction already exists, check if it's a like or dislike
            if reaction.status == Reaction.DISLIKE:
                # Change dislike to like
                reaction.status = Reaction.LIKE
                reaction.save()
                return Response(
                    {'detail': 'Post disliked successfully.'}, status=status.HTTP_200_OK)
            else:
                # Delete the existing like
                reaction.delete()
                return Response(
                    {'detail': 'Post like removed successfully.'}, status=status.HTTP_200_OK)
        else:
            # Create a new like
            reaction.status = Reaction.LIKE
            reaction.save()
            return Response({'detail': 'Post liked successfully.'},
                            status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def dislike(self, request, pk=None):
        post = self.get_object()
        reaction, created = Reaction.objects.get_or_create(
            user=request.user, post=post)
        if not created:
            # Reaction already exists, check if it's a like or dislike
            if reaction.status == Reaction.LIKE:
                # Change like to dislike
                reaction.status = Reaction.DISLIKE
                reaction.save()
                return Response(
                    {'detail': 'Post liked successfully.'}, status=status.HTTP_200_OK)
            else:
                # Delete the existing dislike
                reaction.delete()
                return Response(
                    {'detail': 'Post dislike removed successfully.'}, status=status.HTTP_200_OK)
        else:
            # Create a new dislike
            reaction.status = Reaction.DISLIKE
            reaction.save()
            return Response(
                {'detail': 'Post disliked successfully.'}, status=status.HTTP_201_CREATED)


class MyStoryViewSet(viewsets.ModelViewSet):
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Story.objects.all()

    def get_queryset(self):
        return Story.objects.filter(user=self.request.user).order_by('-pk')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class FollowingStoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = Follow.objects.filter(
            follower=self.request.user).values_list('following', flat=True)
        queryset = Story.objects.filter(user__in=following_users)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class MentionViewSet(viewsets.ModelViewSet):
    serializer_class = MentionSerializer
    filter_fields = ('post', 'user')

    def get_queryset(self):
        return Mention.objects.filter(
            post__user=self.request.user).order_by('-pk')
