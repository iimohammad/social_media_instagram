from django.contrib import admin
from django import forms
from .models import Post, Tag, Reaction, Comment
from django.urls import reverse
from django.utils.html import format_html


class CommentInline(admin.TabularInline):
    model = Comment

    extra = 1
    fields = ('owner', 'reply_to', 'content',)
    show_change_link = True


class PostAdmin(admin.ModelAdmin):
    list_display = ('owner', 'content', 'created_at', 'like_count', 'dislike_count')
    list_filter = ('owner', 'created_at')
    search_fields = ['content__icontains']
    inlines = [CommentInline]


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Reaction)
admin.site.register(Comment)
