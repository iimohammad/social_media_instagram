from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'text', 'created_at')
    list_filter = ('post', 'user', 'created_at')
    search_fields = ('post__title', 'user__username', 'text')
