from django.test import TestCase
from django.urls import reverse
from .factories import UserFactory

class HomeViewTestCase(TestCase):
    """
    Testcase for home view.
    Home view should have:
        * Signup
        * Login
        * Meals
        * Top rated meals
        * About
        * GitHub repo
        * FL logo
    Also as a signed in user it should have:
        * Sign out
        * User Name
        * Upload a meal
        * My Meals
        * Linked to profile page.
    """

    def setUp(self):
        """Setup for Home View."""
        self.response = self.client.get(reverse('home'))

    def test_homeview_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homeview_has_sign_up_link(self):
        '''Test to see if the homepage has register button.'''
        expected = 'accounts/register/'
        self.assertContains(self.response, expected)

    def test_homeview_has_log_in_link(self):
        '''Test to see if the homepage has login button.'''
        expected = 'accounts/login/'
        self.assertContains(self.response, expected)

    def test_homeview_has_meals_link(self):
        '''
        Test to see if the homepage has link to the meals page.
        Need trailing quote mark to distigush this from other links.
        '''
        expected = 'meals/"'
        self.assertContains(self.response, expected)

    def test_homeview_has_meals_top_rated_link(self):
        '''Test to see if the homepage has link to the top rated meals page.'''
        expected = 'meals/top_rated'
        self.assertContains(self.response, expected)

    def test_homeview_has_about_link(self):
        '''Test to see if the homepage has link to the about page.'''
        expected = 'about/'
        self.assertContains(self.response, expected)

    def test_homeview_has_link_to_github(self):
        '''Test to see if the homepage has link to github.'''
        expected = 'https://github.com/FoodLust/FL'
        self.assertContains(self.response, expected)

    def test_homeview_has_food_lust_logo(self):
        '''Test to see if the homepage has food lust logo.'''
        expected = '/static/img/logo.png'
        self.assertContains(self.response, expected)

    def test_homeview_has_logout(self):
        '''Test to see if the homepage has a logout for just logged in users.'''
        expected = 'logout/'
        self.assertNotContains(self.response, expected)
        self.user = UserFactory()
        self.client.force_login(self.user)
        logged_in_response = self.client.get(reverse('home'))
        self.assertContains(logged_in_response, expected)

    def test_homeview_has_userName(self):
        '''Test to see if the homepage has username of a logged in user'''
        self.user = UserFactory()
        expected = self.user.username
        self.assertNotContains(self.response, expected)
        self.client.force_login(self.user)
        logged_in_response = self.client.get(reverse('home'))
        self.assertContains(logged_in_response, expected)

    def test_homeview_has_link_to_upload(self):
        '''Test to see if the homepage has link to upload meals for only members.'''
        self.user = UserFactory()
        expected = 'meals/upload/'
        self.assertNotContains(self.response, expected)
        self.client.force_login(self.user)
        logged_in_response = self.client.get(reverse('home'))
        self.assertContains(logged_in_response, expected)

    def test_homeview_has_link_to_users_meals(self):
        '''Test to see if the homepage has link to users meals for only members.'''
        self.user = UserFactory()
        expected = 'meals/my_meals/'
        self.assertNotContains(self.response, expected)
        self.client.force_login(self.user)
        logged_in_response = self.client.get(reverse('home'))
        self.assertContains(logged_in_response, expected)

    def test_homeview_has_link_to_member_profile_page(self):
        '''Test to see if the homepage has link to users profile for only members.'''
        self.user = UserFactory()
        expected = 'member/'
        self.assertNotContains(self.response, expected)
        self.client.force_login(self.user)
        logged_in_response = self.client.get(reverse('home'))
        self.assertContains(logged_in_response, expected)


class AboutViewTest(TestCase):
    '''TAbout page should have our names on it'''
    def setUp(self):
        """Setup for About View."""
        self.response = self.client.get(reverse('about'))

    def test_about_view_status_code(self):
        '''Test to see if about page has a valid response code.'''
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_has_names(self):
        '''Test to see if the homepage has register button.'''
        names = ['James Canning', 'Zach Rickert', 'Mike Harrison', 'Jeff Torres']
        for name in names:
            self.assertContains(self.response, name)

