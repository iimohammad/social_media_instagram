# logger/views.py
from rest_framework import viewsets
from .models import ViewLog
from .serializers import ViewLogSerializer

class ViewLogViewSet(viewsets.ModelViewSet):
    queryset = ViewLog.objects.all()
    serializer_class = ViewLogSerializer
