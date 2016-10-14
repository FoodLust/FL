from datetime import datetime
from django.test import TestCase
from foodlust.tests.factories import UserFactory, MealFactory, RatingFactory
from meals.models import Comment, Meal
from django.contrib.auth.models import User
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
        self.client.force_login(self.user)
        self.url = reverse('upload_meal')
        self.response = self.client.get(self.url)

    def test_upload_meal(self):
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
        self.client.force_login(self.user)
        self.assertIn('form', self.response.context)

    def test_upload_view_returns_ok_status(self):
        '''test that the response is 200'''
        self.assertEquals(self.response.status_code, 200)

    def test_correct_template(self):
        '''assert view is rendered with our templates'''
        for template_name in ['foodlust/base.html', 'meals/uploads_meal.html']:
            self.assertTemplateUsed(self.response, template_name, count=1)

    def test_upload_view_returns_ok_status(self):
        '''test that the response is 200'''
        self.client.logout()
        self.assertEquals(self.response.status_code, 200)

class MealViewTest(TestCase):
    """Testcase for Meal View."""
    def setUp(self):
        """Setup for Meal view."""
        self.user = User(username='mike')
        self.user.save()
        self.meal = MealFactory()
        self.url = reverse('meal', kwargs={
                           'pk': str(self.meal.pk)}
                           )
        self.client.force_login(self.user)
        self.response = self.client.get(self.url)
        

    def test_status_code(self):
        """Test status code for meal detail view."""
        self.assertEqual(self.response.status_code, 200)

    def test_meal_detail_view_template(self):
        """Test template of meal detail view."""
        self.assertContains(self.response, '<p>Comments:</p>')

    def test_meal_view_has_meal_title(self):
        """Test view has meal and title."""
        self.assertContains(self.response, self.meal.title)

    def test_meal_view_has_not_yet_rated(self):
        """Test template contains not yet rated."""
        self.assertContains(self.response, 'Not yet rated')

class CommentTestCase(TestCase):
    """Test module for the comments model."""
    def setUp(self):
        self.meal = MealFactory()
        self.user = User(username='Guy')
        self.user.save()
        self.comment = Comment()
        self.comment.meal = self.meal
        self.comment.user = self.user
        self.comment.save()

    def test_comment_has_message(self):
        """Test comment model has attribute message."""
        self.assertTrue(hasattr(self.comment, 'message'))

    def test_comment_meal_is_a_meal(self):
        """Test to see if the meal that is on test comment is a meal."""
        self.assertTrue(isinstance(self.comment.meal, Meal))

    def test_comment_user(self):
        """Test to see if comment is from a user."""
        self.assertTrue(isinstance(self.comment.user, User))

    def test_comment_date(self):
        """Test to see if comment is from a user."""
        format_string = "%Y-%m-%d"
        expected_date = datetime.utcnow().strftime(format_string)
        date = self.comment.date_created.strftime(format_string)
        self.assertEqual(expected_date, date)


