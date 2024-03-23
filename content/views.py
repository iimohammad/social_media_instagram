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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            return Response({"error": "You don't have permission to update this post."}, status=status.HTTP_403_FORBIDDEN)

        content_data = request.data.pop('content', None)
        if content_data:
            instance.content.all().delete()
            for content_item in content_data:
                PostContent.objects.create(post=instance, **content_item)
        return super().update(request, *args, **kwargs)

class FollowingPostViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowingPostSerializer

    def get_queryset(self):
        following_users = Follow.objects.filter(follower=self.request.user).values_list('following', flat=True)
        queryset = Post.objects.filter(user__in=following_users)
        return queryset
    
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        reaction, created = Reaction.objects.get_or_create(user=request.user, post=post)
        if not created:
            # Reaction already exists, check if it's a like or dislike
            if reaction.status == Reaction.DISLIKE:
                # Change dislike to like
                reaction.status = Reaction.LIKE
                reaction.save()
                return Response({'detail': 'Post disliked successfully.'}, status=status.HTTP_200_OK)
            else:
                # Delete the existing like
                reaction.delete()
                return Response({'detail': 'Post like removed successfully.'}, status=status.HTTP_200_OK)
        else:
            # Create a new like
            reaction.status = Reaction.LIKE
            reaction.save()
            return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def dislike(self, request, pk=None):
        post = self.get_object()
        reaction, created = Reaction.objects.get_or_create(user=request.user, post=post)
        if not created:
            # Reaction already exists, check if it's a like or dislike
            if reaction.status == Reaction.LIKE:
                # Change like to dislike
                reaction.status = Reaction.DISLIKE
                reaction.save()
                return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_200_OK)
            else:
                # Delete the existing dislike
                reaction.delete()
                return Response({'detail': 'Post dislike removed successfully.'}, status=status.HTTP_200_OK)
        else:
            # Create a new dislike
            reaction.status = Reaction.DISLIKE
            reaction.save()
            return Response({'detail': 'Post disliked successfully.'}, status=status.HTTP_201_CREATED)
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
    filter_fields = ('post', 'user')

    def get_queryset(self):
        return Mention.objects.filter(post__user=self.request.user).order_by('-pk')



# class FollowingPostViewSet(viewsets.ReadOnlyModelViewSet):
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
#     filter_fields = ('user',)
#     search_fields = ('caption',)

#     def get_queryset(self):
#         user = self.request.user
#         following_users = user.following.all().values_list('following', flat=True)
#         return Post.objects.filter(user__in=following_users).order_by('-pk')


# class FollowingStoryViewSet(BaseStoryRelatedViewSet):
#     serializer_class = StorySerializer
#     permission_classes = [permissions.IsAuthenticated]
#     filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
#     filter_fields = ('user',)

#     def get_queryset(self):
#         user = self.request.user
#         following_users = user.following.all().values_list('following', flat=True)
#         return Story.objects.filter(user__in=following_users).order_by('-pk')
