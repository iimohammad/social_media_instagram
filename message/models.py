from django.db import models
from django.conf import settings


class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class TextMessage(Message):
    test = models.TextField()


class ImageMessage(Message):
    image = models.ImageField(upload_to='message_photos/', blank=False)


class AudioMessage(Message):
    audio_file = models.FileField(upload_to='message_audio/', blank=False)
