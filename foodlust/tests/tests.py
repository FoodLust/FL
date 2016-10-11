from django.test import TestCase
from django.urls import reverse


class HomeViewTestCase(TestCase):
    """Testcase for home view."""

    def setUp(self):
        """Setup for Home View."""
        self.response = self.client.get(reverse('home'))

    def test_homeview_status_code(self):
        self.assertEqual(self.response.status_code, 200)
