from django.contrib import admin
from django.urls import path, include
from social_media.local_settings import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from home.views import home

urlpatterns = [
    path(ADMIN, admin.site.urls),
    path('', home),
    path('content/', include('content.urls')),
    path('user_panel/',include('user_panel.urls'),name='user-panel-url'),
    path('',include('user_panel.urls')),
    path('user_activity/', include('user_activity.urls')),
    # path('api/logger/', include('logger.urls')),
    # path('api/direct_message/', include('direct_message.urls')),
    #

# SimpleJWT URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api-auth/', include('rest_framework.urls')),
]
