from django.db import models
from django.conf import settings

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Post(BaseModel):
    caption = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def delete(self):
        for content in self.content_objects.all():
            content.delete()
        super().delete()

    def __str__(self):
        return self.caption

class Content(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='content_objects')

    def delete(self):
        super().delete()

    def __str__(self):
        return f"Content for post: {self.post.caption}"

class Story(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Stories'

    def __str__(self):
        return str(self.id)

class Mention(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='mentions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['post', 'user']]

    def __str__(self):
        return str(self.id)

class Hashtag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='hashtags')
    title = models.CharField(max_length=255)

    class Meta:
        unique_together = [['post', 'title']]

    def __str__(self):
        return self.title

class ContentImage(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='content_images/')

    def delete(self):
        storage, path = self.image.storage, self.image.path
        storage.delete(path)
        super().delete()

    def __str__(self):
        return str(self.id)
