from django.db import models
from django.conf import settings

from user_panel.models import CustomUser, Follow


class Message(models.Model):
    sender = models.ForeignKey(
        CustomUser, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        CustomUser, related_name='received_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    TextContent = models.TextField(blank = True)
    file = models.FileField(upload_to='message_files/',blank=True)


    def __str__(self):
        return str(self.id)
    

