from django.contrib import admin
from .models import Comment, PostLike, StoryLike


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'text', 'created_at')
    list_filter = ('post', 'user', 'created_at')
    search_fields = ('post__title', 'user__username', 'text')


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'created_at')
    list_filter = ('post', 'user', 'created_at')
    search_fields = ('post__title', 'user__username')


@admin.register(StoryLike)
class StoryLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'story_image', 'user', 'created_at')
    list_filter = ('story_image', 'user', 'created_at')
    search_fields = ('story_image__title', 'user__username')
