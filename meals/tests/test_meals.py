from django.test import TestCase
from foodlust.tests.factories import UserFactory, MealFactory, RatingFactory
from django.urls import reverse
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


class RatingTestCase(TestCase):

    def setUp(self):
        self.rating = RatingFactory()

    def test_rating(self):
        self.assertTrue(self.rating.like)


class MealUploadTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.url = reverse('upload_meal')

    def test_upload_meal(self):
        self.client.force_login(self.user)
        with open(TEST_PHOTO_PATH, 'rb') as fh:
            data = {
                'title': 'test_title',
                'photo': fh,
                'member': self.user.member.pk,
            }
            # import pdb; pdb.set_trace()
            respones = self.client.post(self.url, data)
        self.assertEqual(respones.status_code, 302)



