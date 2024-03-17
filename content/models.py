from django.db import models


class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    video = models.FileField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post {self.id}"


class Story(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='stories/', null=True, blank=True)
    video = models.FileField(upload_to='stories/', null=True, blank=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return f"Story {self.id}"
