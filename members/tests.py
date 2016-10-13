from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from foodlust.tests.factories import UserFactory, MealFactory


class MemberTestCase(TestCase):
    """ This class will establish the test cases for the member model."""

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
        self.response = self.client.get(reverse('registration_register'))
    
    def test_register_view_status_code(self):
        """Test status code is 200."""
        self.assertEqual(self.response.status_code, 200)

    def test_register_view_has_form(self):
        """Test if template has form"""
        self.assertContains(self.response, "</form>")

    def test_register_failure(self):
        """Test register with bad creditinals."""
        self.assertEqual(
            self.client.post(reverse('registration_register'), {}).status_code,
            200)


class TestMemberView(TestCase):
    """Test profile view."""

    def setUp(self):
        """Set up for authenticated user."""
        self.user = User(username="mike", first_name='mike')
        self.user.save()

    def test_member_page_status_code(self):
        """Test member page status code."""
        self.client.force_login(self.user)
        self.assertEqual(self.client.get(reverse('member')).status_code, 200)

    def test_login_required(self):
        """Test member page requires login."""
        self.client.logout()
        self.assertEqual(self.client.get(reverse('member')).status_code, 302)

    def test_template_has_profile_tag(self):
        """Test template contains the word profile."""
        self.client.force_login(self.user)
        response = self.client.get(reverse('member'))
        self.assertContains(response, '<h1>Profile</h1>')

    def test_template_contains_username(self):
        """Test member page has username."""
        self.client.force_login(self.user)
        response = self.client.get(reverse('member'))
        self.assertContains(response, self.user.username)

    def test_template_contains_first_name(self):
        """Test member page has first name."""
        self.client.force_login(self.user)
        response = self.client.get(reverse('member'))
        self.assertContains(response, 'mike')

    def test_meals_on_member_page(self):
        """Test meals show up on member page."""
        self.meal = MealFactory()
        self.client.force_login(self.user)
        response = self.client.get(reverse('member'))
        self.assertContains(response, self.meal.id)

class TestEditMemberView(TestCase):
    """Testcase for edit member info."""

    def setUp(self):
        """Setup for testcase."""
        self.user = User(username="mike", first_name='mike')
        self.user.save()
        self.client.force_login(self.user)
        self.response = self.client.get(reverse('member_edit'))

    def test_memebr_edit_status_code_authd(self):
        """Test status code 200 for authenticated user for edit."""
        self.assertEqual(self.response.status_code, 200)

    def test_member_edit_contains_edit(self):
        """Test edit page contains edit profile."""
        self.assertContains(self.response, 'Edit')