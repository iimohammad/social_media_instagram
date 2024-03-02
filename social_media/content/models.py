from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


def user_directory_path(instance, filename):
    return f'user_{instance.owner.id}/{filename}'


class Media:
    pass


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    image = models.FileField(upload_to=user_directory_path, null=True, blank=True, verbose_name="Post Image",
                             help_text="Only jpg/jpeg files are allowed.")
    content = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    # return f"{self.owner.username} {self.created_at}"

    def like_count(self):
        return self.reactions.filter(status='1').count()

    def dislike_count(self):
        return self.reactions.filter(status='2').count()


class Reaction(models.Model):
    STATUS_CHOICES = [('1', 'like'), ('2', 'dislike')]
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1')

    class Meta:
        unique_together = ('owner', 'post')


