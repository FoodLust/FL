from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class MemberTestCase(TestCase):
    """ This class will establish the test cases for the member model """

    def setUp(self):
        """ Setup for Member model test """
        self.user = User(username='Test User', first_name='Test')
        self.user.save()

    def test_user_is_member(self):
        """ Test to confirm that user is a member """
        self.assertTrue(hasattr(self.user, 'member'))

    def test_user_name(self):
        """ Test to confirm username is correct on member model """
        self.assertEqual(self.user.username, 'Test User')

    def test_member_string_method(self):
        """ Test to confirm member string method prints correctly """
        self.assertEqual(str(self.user.member), 'Test')

    def test_member_is_active(self):
        """ Test to confirm member is made active upon registration """
        self.assertTrue(self.user.member.active)

class TestRegistrationView(TestCase):
    """Test Registration View."""

    def setUp(self):
        """Set up registration."""
        self.resposne = self.client.get(reverse('registration_register'))
    
    def test_register_view_status_code(self):
        """Test status code is 200."""
        assertEqual(self.response.status_code, 200)