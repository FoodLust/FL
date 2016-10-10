from django.test import TestCase
from foodlust.tests.factories import MemberFactory, MealFactory, RattingFactory
import os
from io import open


HERE = os.path.dirname(os.path.abspath(__file__))
TEST_PHOTO_PATH = os.path.join(HERE, 'testimg.png')


class MealTestCase(TestCase):

    def setUp(self):
        self.meal = MealFactory()

    def test_meal_creation(self):
        self.assertEqual(self.meal.title, 'Test meal')
        self.assertTrue(hasattr(self.meal.member, 'username'))
        self.assertTrue(hasattr(self.meal, 'photo'))


class RattingTestCase(TestCase):

    def setUp(self):
        self.ratting = RattingFactory()

    def test_ratting(self):
        self.assertTrue(self.ratting.like)


class MealUploadTestCase(TestCase):

    def setUp(self):
        self.member = MemberFactory()

    def test_upload_meal(self):
        with open(TEST_PHOTO_PATH, 'rb') as fh:
            data = {
                'title': 'test_title',
                'photo': fh,
                'member': self.user.pk,
            }
            respones = self.client.post(self.url, data)
        self.assertEqual(respones.status_code, 302)



