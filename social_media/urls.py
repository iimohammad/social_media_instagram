from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/content/', include('content.urls')),
    path('api/userarea/', include('userarea.urls')),
    path('api/useractivities/', include('useractivities.urls')),
    path('api/logs/', include('logs.urls')),
    path('api/directmessaging/', include('directmessaging.urls')),
]
