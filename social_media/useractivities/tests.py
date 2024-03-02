from django.test import TestCase
from .models import Comment, Like


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Comment.objects.create(comment_text='Test comment.')

    def test_comment_content(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = f'{comment.comment_text}'
        self.assertEqual(expected_object_name, 'Test comment.')


class LikeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Like.objects.create()

    def test_like_instance(self):
        like = Like.objects.get(id=1)
        self.assertTrue(isinstance(like, Like))
