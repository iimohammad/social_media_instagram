from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


def validate_image_extension(value):
    valid_extensions = ['.jpg', '.jpeg']
    extension = str(value.name.split('.')[-1]).lower()
    if extension not in valid_extensions:
        raise ValidationError("Only JPEG and JPG files are allowed.")


class User(AbstractUser):
    followings = models.ManyToManyField(
        'self',
        related_name='followers',
        symmetrical=False,
        blank=True
    )
    bio = models.CharField(max_length=50)
    profile_image = models.FileField(
        null=True,
        blank=True,
        verbose_name="Profile Image",
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg']),
            validate_image_extension,
        ]
    )

    def display_name(self):
        if not self.first_name and not self.last_name:
            return self.username
        else:
            return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username

    def following_count(self):
        return self.followings.count()

    def followers_count(self):
        return self.followers.count()
