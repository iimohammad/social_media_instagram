from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(UserAdmin):
    list_display = ('username', 'full_name', 'is_active', 'following_count', 'followers_count')
    list_filter = ('is_active',)
    search_fields = ('username',)

    def full_name(self, obj):
        return obj.display_name()

    full_name.short_description = 'full name'

admin.site.register(User, UserAdmin)