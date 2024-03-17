from django.db import models
from django.contrib.auth.models import User

from content.models import Post


class ContentLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Content Log for {self.user.username} on Post {self.post.id}"


class ProfileLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_logs')
    viewed_profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='viewed_profile_logs')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile Log for {self.user.username} viewing {self.viewed_profile.username}'s profile"
