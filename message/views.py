# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions
from user_panel.models import Follow
from user_panel.models import CustomUser
from .models import Message
from .serializers import MessageReceiveSerializers, MessageSendSerializers


class ShowMyRecieveMessageViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MessageReceiveSerializers

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user)


class SendMessageViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MessageSendSerializers

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user)
