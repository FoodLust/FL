from django.test import TestCase
from django.urls import urls

class HomeViewTestCase(TestCase):
    """Testcase for home view."""

    def setUp(self):
        """Setup for Home View."""
        self.response = self.client.get(reverse('home'))