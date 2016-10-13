from django.test import TestCase
from django.urls import reverse
from .factories import MealFactory


class HomeViewTestCase(TestCase):
    """Testcase for home view."""

    def setUp(self):
        """Setup for Home View."""
        self.meal = MealFactory()

        # self.response = self.client.get(reverse('home'))

    def tearDown(self):
        pass

    # def test_homeview_status_code(self):
    #     self.assertEqual(self.response.status_code, 200)

    # def test_homeview_contains_login(self):
    #     self.assertContains(self.response.status_code, 200)

    # def test_home_page_exists(self):
    #     """assert that the response for the homepage url is 200"""
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)
    
    def test_for_registration_button(self):
        pass

class FindPageTest(TestCase):
    def test_homeview_exists(self):
        response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200)

    def test_about_view_exists(self):
        response = self.client.get('about/')
        self.assertEqual(self.response.status_code, 200)

