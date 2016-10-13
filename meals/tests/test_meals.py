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
        for template_name in ['foodlust/base.html', 'meals/uploads_meal.html']:
            self.assertTemplateUsed(self.response, template_name, count=1)


class MealViewTest(TestCase):
    def setUp(self):
        self.meal = MealFactory()
        self.url = reverse('meal', kwargs={
                           'username': self.meal.member.username,
                           'pk': str(self.meal.member.pk)}
                           )
        self.response = self.client.get(self.url)

    # def test_correct_template(self):
    #     '''assert view is rendered with our templates'''
    #     for template_name in ['foodlust/base.html', 'meals/meal.html']:
    #         self.assertTemplateUsed(self.response, template_name, count=1)   


class FindPageTest(TestCase):
    '''Test to see if views will return a 200 status code.'''
    def test_meals_page_exists(self):
        """assert that the response for the meals url is 200"""
        response = self.client.get('/meals/')
        self.assertEqual(response.status_code, 200)

    def test_meal_upload_page_exists(self):
        """assert that the response for the homepage url is 200"""
        response = self.client.get('/meals/upload/')
        self.assertEqual(response.status_code, 200)

    def test_meal_detail_page_exists(self):
        """assert that the response for the detail meal view url is 200"""
        meal = MealFactory()
        meal_id = meal.pk
        path = '/meals/' + str(meal_id)
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)

    def test_meals_by_rating_page_exists(self):
        """assert that the response for the meals by rating url is 200"""
        path = '/meals/by_rating/'
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)

    def test_meals_by_user_page_exists(self):
        """assert that the response for the meals by user url is 200"""
        user = UserFactory()
        username =user.username
        path = '/meals/' + username + '/'
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
