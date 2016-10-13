from django.test import TestCase
from django.urls import reverse
from .factories import MealFactory


class HomeViewTestCase(TestCase):
    """Testcase for home view."""

    def setUp(self):
        """Setup for Home View."""
        # self.response = self.client.get(reverse('home'))

    def tearDown(self):
        pass

    # def test_homeview_contains_login(self):
    #     self.assertContains(self.response.status_code, 200)

    # def test_home_page_exists(self):
    #     """assert that the response for the homepage url is 200"""
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)
    
    def test_for_registration_button(self):
        """Test to see if login page has link to registration."""
        pass

class FindPageTest(TestCase):
    def test_homeview_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_view_exists(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

