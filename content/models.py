from django.db import models
from django.conf import settings
from .validators import validate_file_extension, validate_hashtag
from django.core.exceptions import ValidationError


class Post(models.Model):
    caption = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def like_count(self):
        return self.reactions.filter(status=Reaction.LIKE).count()

    def dislike_count(self):
        return self.reactions.filter(status=Reaction.DISLIKE).count()

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.caption

# This types of writing model support multiple slide model


class PostContent(models.Model):
    POST_CONTENT_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]
    post = models.ForeignKey(
        Post, related_name='content', on_delete=models.CASCADE)
    typeContent = models.CharField(max_length=10, choices=POST_CONTENT_CHOICES)
    file = models.FileField(upload_to='post_content/', null=True)

    def delete(self):
        storage, path = self.file.storage, self.file.path
        storage.delete(path)
        super().delete()

    def __str__(self):
        return f"Content for post: {self.post.caption}"


class Hashtag(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='hashtags')
    tag = models.CharField(max_length=30, validators=[validate_hashtag])

    class Meta:
        unique_together = [['post', 'tag']]

    def __str__(self):
        return self.tag


class Story(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='content/',
                            validators=[validate_file_extension])

    class Meta:
        verbose_name_plural = 'Stories'

    def __str__(self):
        return str(self.id)


class StoryContent(models.Model):
    STORY_CONTENT_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]
    story = models.ForeignKey(
        Story, related_name='story_content', on_delete=models.CASCADE)
    typeContent = models.CharField(
        max_length=10, choices=STORY_CONTENT_CHOICES)
    file = models.FileField(upload_to='post_content/')

    def delete(self):
        storage, path = self.file.storage, self.file.path
        storage.delete(path)
        super().delete()

    def __str__(self):
        return f"Content for post: {self.post.caption}"


class Mention(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='mentions')

    class Meta:
        unique_together = [['post', 'user']]

    def clean(self):
        if self.user == self.post.user:
            raise ValidationError(
                "You cannot mention yourself in your own post.")

    def __str__(self):
        return str(self.id)


class Reaction(models.Model):
    LIKE = 'like'
    DISLIKE = 'dislike'
    STATUS_CHOICES = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='reactions', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        unique_together = [['user', 'post']]

    def __str__(self):
        return f'{self.user.username} reacted {
            self.status} to post "{self.post.caption}"'
