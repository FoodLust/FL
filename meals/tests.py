from django.test import TestCase
from foodlust.tests.factories import MemberFactory, MealFactory, RattingFactory


class MealTestCase(TestCase):

    def setUp(self):
        self.meal = MealFactory()

    def test_meal_creation(self):
        self.assertEqual(self.meal.title, 'Test meal')
        self.assertTrue(hasattr(self.meal.member, 'username'))
        self.assertTrue(hasattr(self.meal, 'photo'))


class RattingTestCase(TestCase):

    def setUp(self):
        self.ratting = RattingFactory()

    def test_ratting(self):
        self.assertTrue(self.ratting.like)
