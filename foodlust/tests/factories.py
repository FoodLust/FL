import factory
from django.contrib.auth.models import User
from meals.models import Meal, Ratting


class MemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user{}".format(n))
    first_name = factory.Sequence(lambda n: "user{}".format(n))


class MealFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Meal

    member = factory.SubFactory(MemberFactory)
    photo = factory.django.ImageField(color='red')
    title = 'Test meal'


class RattingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ratting

    member = factory.SubFactory(MemberFactory)
    meal = factory.SubFactory(MealFactory)
    like = True
