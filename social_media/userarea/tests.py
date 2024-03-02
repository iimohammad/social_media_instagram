from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='testuser', password='testpassword')
        UserProfile.objects.create(user=user, bio='Test bio.')

    def test_bio_content(self):
        profile = UserProfile.objects.get(id=1)
        expected_object_name = f'{profile.bio}'
        self.assertEqual(expected_object_name, 'Test bio.')
