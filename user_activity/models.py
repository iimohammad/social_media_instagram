from django.db import models
from django.conf import settings
from content.models import *


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class BaseLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PostLike(BaseLike):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = [['user', 'post']]

    def __str__(self):
        return f'Like by {self.user.username} on post {self.post.id}'


class StoryLike(BaseLike):
    story_image = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = [['user', 'story_image']]

    def __str__(self):
        return f'Like by {self.user.username} on story image {self.story_image.id}'
