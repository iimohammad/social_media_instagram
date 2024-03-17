from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import CommentSerializer
from rest_framework.views import APIView
from .models import Comment, PostLike, StoryLike
from content.models import *
class CommentViewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostLikeViewSet(viewsets.ViewSet):
    def create(self, request, post_id, *args, **kwargs):
        try:
            # Check if the post exists
            post = Post.objects.get(pk=post_id)
            # Check if the user has already liked the post
            if PostLike.objects.filter(post=post, user=request.user).exists():
                return Response({"error": "Post already liked by the user"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Create a new like for the post
                like = PostLike.objects.create(post=post, user=request.user)
                return Response(status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, post_id, *args, **kwargs):
        try:
            # Check if the post exists
            post = Post.objects.get(pk=post_id)
            # Check if the user has already liked the post
            like = PostLike.objects.filter(post=post, user=request.user).first()
            if like:
                # Delete the like
                like.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "User has not liked the post"}, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

class StoryLikeViewSet(viewsets.ViewSet):
    def create(self, request, story_image_id, *args, **kwargs):
        try:
            # Check if the story image exists
            story_image = Story.objects.get(pk=story_image_id)
            # Check if the user has already liked the story image
            if StoryLike.objects.filter(story_image=story_image, user=request.user).exists():
                return Response({"error": "Story image already liked by the user"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Create a new like for the story image
                like = StoryLike.objects.create(story_image=story_image, user=request.user)
                return Response(status=status.HTTP_200_OK)
        except Story.DoesNotExist:
            return Response({"error": "Story image not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, story_image_id, *args, **kwargs):
        try:
            # Check if the story image exists
            story_image = Story.objects.get(pk=story_image_id)
            # Check if the user has already liked the story image
            like = StoryLike.objects.filter(story_image=story_image, user=request.user).first()
            if like:
                # Delete the like
                like.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "User has not liked the story image"}, status=status.HTTP_400_BAD_REQUEST)
        except Story.DoesNotExist:
            return Response({"error": "Story image not found"}, status=status.HTTP_404_NOT_FOUND)
