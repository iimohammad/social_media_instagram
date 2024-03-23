# logger/serializers.py
from rest_framework import serializers
from .models import ViewLog


class ViewLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewLog
        fields = ['id', 'user', 'viewed_at',
                  'content_type', 'object_id', 'content_object']
