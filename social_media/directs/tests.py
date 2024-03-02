from django.test import TestCase
from .models import Message


class MessageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Message.objects.create(message_text='Test message.')

    def test_message_content(self):
        message = Message.objects.get(id=1)
        expected_object_name = f'{message.message_text}'
        self.assertEqual(expected_object_name, 'Test message.')
