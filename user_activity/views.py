from rest_framework.response import Response

from content.serializers import FollowingPostSerializer
from .serializers import CommentSerializer
from .models import Comment
from content.models import *
from rest_framework.decorators import action
from rest_framework import viewsets, filters, permissions, status
from user_panel.models import Follow



class LikeFollowingPostViewSet(viewsets.ReadOnlyModelViewSet):
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
        

class FollowingCommentViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        following_users = Follow.objects.filter(follower=self.request.user).values_list('following', flat=True)
        queryset = Comment.objects.filter(post__user__in=following_users)
        return queryset
    

class MyCommentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.filter(post__user=self.request.user)
        return queryset