from django.contrib import admin
from .models import Post, Story, Mention, Hashtag, ContentImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'user', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('caption', 'user__username')


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username',)


@admin.register(Mention)
class MentionAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user')
    list_filter = ('post', 'user')
    search_fields = ('user__username',)


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'title')
    list_filter = ('post', 'title')
    search_fields = ('title',)


@admin.register(ContentImage)
class ContentImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'image')
    search_fields = ('content__post__caption',)
