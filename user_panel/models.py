from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', blank=True, null=True)
    is_public = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['user']),
        ]

    def __str__(self):
        return f"Profile of {self.user.username}"


class Follow(models.Model):
    follower = models.ForeignKey(
        CustomUser,
        related_name='following_set',
        on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        CustomUser,
        related_name='followers_set',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['follower', 'following']
        verbose_name = 'Follow'
        verbose_name_plural = 'Follows'

    def __str__(self):
        return f"{self.follower} follows {self.following}"

    def clean(self):
        if self.follower == self.following:
            raise ValidationError("A user cannot follow themselves.")
