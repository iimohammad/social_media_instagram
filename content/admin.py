from django.contrib import admin
from .models import Post, PostContent, Hashtag, Story, StoryContent, Mention, Reaction


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'user', 'created_at',
                    'like_count', 'dislike_count')
    list_filter = ('user', 'created_at')
    search_fields = ('caption', 'user__username')


@admin.register(PostContent)
class PostContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'typeContent')
    list_filter = ('typeContent',)
    search_fields = ('post__caption',)


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'tag')
    search_fields = ('tag',)


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username',)


@admin.register(StoryContent)
class StoryContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'story', 'typeContent')
    list_filter = ('typeContent',)
    search_fields = ('story__id',)


@admin.register(Mention)
class MentionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post')
    search_fields = ('user__username', 'post__caption')


@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'status')
    list_filter = ('status',)
    search_fields = ('user__username', 'post__caption')
