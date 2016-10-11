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
        self.response = self.client.get(self.url)

    def test_upload_meal(self):
        self.client.force_login(self.user)
        with open(TEST_PHOTO_PATH, 'rb') as fh:
            data = {
                'title': 'test_title',
                'photo': fh,
                'member': self.user.member.pk,
            }
            respones = self.client.post(self.url, data)
        self.assertEqual(respones.status_code, 302)

    def test_form_present_in_context(self):
        """test there is a form on the add meal"""
        self.assertIn('form', self.response.context)

    def test_upload_view_returns_ok_status(self):
        '''test that the response is 200'''
        self.assertEquals(self.response.status_code, 200)

    def test_correct_template(self):
        '''assert view is rendered with our templates'''
        for template_name in ['foodlust/base.html', 'meal/upload_meal.html']:
            self.assertTemplateUsed(self.response, template_name, count=1)
