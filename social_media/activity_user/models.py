from django.db import models
from django.conf import settings

from social_media.content.models import Post


class Comment(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.reply_to:
            self.post = self.reply_to.post
        super().save(*args, **kwargs)
