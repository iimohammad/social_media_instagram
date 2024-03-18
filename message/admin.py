from django.contrib import admin
from .models import TextMessage, ImageMessage, AudioMessage


@admin.register(TextMessage)
class TextMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'created_at', 'test')
    list_filter = ('sender', 'receiver', 'created_at')
    search_fields = ('sender__username', 'receiver__username', 'test')


@admin.register(ImageMessage)
class ImageMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'created_at', 'image')
    list_filter = ('sender', 'receiver', 'created_at')
    search_fields = ('sender__username', 'receiver__username')


@admin.register(AudioMessage)
class AudioMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'created_at', 'audio_file')
    list_filter = ('sender', 'receiver', 'created_at')
    search_fields = ('sender__username', 'receiver__username')
