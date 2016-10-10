from django.test import TestCase
from django.contrib.auth.models import User


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
