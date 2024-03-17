from rest_framework import serializers
from user_panel.models import CustomUser
from .models import TestMessage, ImageMessage, AudioMessage

class sender_receiver_serializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username']



class TestMessageSerializer(serializers.ModelSerializer):
    sender_info = sender_receiver_serializer(source='sender', read_only=True)

    class Meta:
        model = TestMessage
        fields = ('id', 'sender', 'sender_info', 'test', 'created_at')

    def get_fields(self):
        fields = super().get_fields()
        if 'sender' in fields:
            fields['sender'].read_only = True
        return fields

class ImageMessageSerializer(serializers.ModelSerializer):
    sender_info = sender_receiver_serializer(source='sender', read_only=True)

    class Meta:
        model = ImageMessage
        fields = ('id', 'sender', 'sender_info', 'image', 'created_at')

    def get_fields(self):
        fields = super().get_fields()
        if 'sender' in fields:
            fields['sender'].read_only = True
        return fields

class AudioMessageSerializer(serializers.ModelSerializer):
    sender_info = sender_receiver_serializer(source='sender', read_only=True)

    class Meta:
        model = AudioMessage
        fields = ('id', 'sender', 'sender_info', 'audio_file', 'created_at')

    def get_fields(self):
        fields = super().get_fields()
        if 'sender' in fields:
            fields['sender'].read_only = True
        return fields
