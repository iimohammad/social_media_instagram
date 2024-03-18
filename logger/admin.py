from django.contrib import admin
from .models import ViewLog


class ViewLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'viewed_at', 'content_type', 'object_id')
    list_filter = ('user', 'viewed_at', 'content_type')
    search_fields = ('user__username', 'content_type__name', 'object_id')


admin.site.register(ViewLog, ViewLogAdmin)
