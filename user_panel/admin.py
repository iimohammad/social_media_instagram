from django.contrib import admin
from .models import CustomUser, Profile, Follow
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from import_export.admin import ImportExportActionModelAdmin
from .resource import UserResource


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'


class FollowInline(admin.TabularInline):
    model = Follow
    fk_name = 'follower'
    extra = 1


class FollowedByInline(admin.TabularInline):
    model = Follow
    fk_name = 'following'
    verbose_name_plural = 'Followed By'
    extra = 0


class ProfileOwnedInline(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'Owned Profile'
    can_delete = False
    fk_name = 'user'


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin, ImportExportActionModelAdmin):
    inlines = (ProfileInline, FollowInline,
               FollowedByInline, ProfileOwnedInline)
    list_display = ('id', 'username', 'email', 'first_name',
                    'last_name', 'phone_number')
    ordering = ['id']
    search_fields = ('username', 'email', 'first_name',
                     'last_name', 'phone_number')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name',
         'last_name', 'email', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    resource_class = UserResource


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower', 'following', 'created_at')
    search_fields = ('follower__username', 'following__username')
    ordering = ['id']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio')
    search_fields = ('user__username', 'bio')
    ordering = ['id']
