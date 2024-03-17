from django.contrib import admin
from .models import ContentLog, ProfileLog

admin.site.register(ContentLog)
admin.site.register(ProfileLog)
