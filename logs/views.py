from rest_framework import generics
from .models import ContentLog, ProfileLog
from .serializers import ContentLogSerializer, ProfileLogSerializer


class ContentLogListCreateAPIView(generics.ListCreateAPIView):
    queryset = ContentLog.objects.all()
    serializer_class = ContentLogSerializer


class ProfileLogListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProfileLog.objects.all()
    serializer_class = ProfileLogSerializer
