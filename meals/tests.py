from django.test import TestCase
from foodlust.test.factories import MemberFactory, MealFactory



class MealTestCase(TestCase):

    def setUp(self):
        self.user = MemberFactory.create()
        self.client.force_login(user=self.user)

    def test_meal_creation(self):
        self.meal = MealFactory()
