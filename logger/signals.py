from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ViewLog
from content.models import *
from user_panel.models import *


@receiver(post_save, sender=Post)
def log_post_view(sender, instance, created, **kwargs):
    if created:
        ViewLog.objects.create(user=instance.user, content_object=instance)


@receiver(post_save, sender=Story)
def log_story_view(sender, instance, created, **kwargs):
    if created:
        ViewLog.objects.create(user=instance.user, content_object=instance)


@receiver(post_save, sender=Profile)
def log_profile_view(sender, instance, created, **kwargs):
    if created:
        ViewLog.objects.create(user=instance.user, content_object=instance)
