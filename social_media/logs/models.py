# logs/models.py
from django.db import models
from django.contrib.auth import get_user_model

from social_media.content.models import Post, Story

User = get_user_model()


class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    content = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, null=True, blank=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
