# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import TestMessage, ImageMessage, AudioMessage
from .serializers import TestMessageSerializer, ImageMessageSerializer, AudioMessageSerializer

class SendMessageAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = None
        message_type = request.data.get('type')
        
        if message_type == 'test':
            serializer = TestMessageSerializer(data=request.data)
        elif message_type == 'image':
            serializer = ImageMessageSerializer(data=request.data)
        elif message_type == 'audio':
            serializer = AudioMessageSerializer(data=request.data)
        
        if serializer is not None and serializer.is_valid():
            serializer.save(sender=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReceiveMessageAPIView(APIView):
    def get(self, request, *args, **kwargs):
        test_messages = TestMessage.objects.filter(receiver=request.user)
        image_messages = ImageMessage.objects.filter(receiver=request.user)
        audio_messages = AudioMessage.objects.filter(receiver=request.user)

        test_serializer = TestMessageSerializer(test_messages, many=True)
        image_serializer = ImageMessageSerializer(image_messages, many=True)
        audio_serializer = AudioMessageSerializer(audio_messages, many=True)

        return Response({
            'test_messages': test_serializer.data,
            'image_messages': image_serializer.data,
            'audio_messages': audio_serializer.data
        }, status=status.HTTP_200_OK)

class TestMessageList(generics.ListAPIView):
    queryset = TestMessage.objects.all()
    serializer_class = TestMessageSerializer

class ImageMessageList(generics.ListAPIView):
    queryset = ImageMessage.objects.all()
    serializer_class = ImageMessageSerializer

class AudioMessageList(generics.ListAPIView):
    queryset = AudioMessage.objects.all()
    serializer_class = AudioMessageSerializer