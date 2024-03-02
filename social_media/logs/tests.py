from django.test import TestCase
from .models import ContentLog, ProfileLog

class ContentLogModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ContentLog.objects.create(action='Test action.')

    def test_action_content(self):
        log = ContentLog.objects.get(id=1)
        expected_object_name = f'{log.action}'
        self.assertEqual(expected_object_name, 'Test action.')
