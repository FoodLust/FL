import factory
from django.contrib.auth.models import User
from meals.models import Meal, Rating
from member.models import Member


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user{}".format(n))
    first_name = factory.Sequence(lambda n: "user{}".format(n))


class MealFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Meal

    member = factory.SubFactory(UserFactory)
    photo = factory.django.ImageField(color='red')
    title = 'Test meal'


class RatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Rating

    member = factory.SubFactory(UserFactory)
    meal = factory.SubFactory(MealFactory)
    like = True


class MemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Member

    username = factory.Sequence(lambda n: "user{}".format(n))
    first_name = factory.Sequence(lambda n: "user{}".format(n))
    email = factory.Sequence(lambda n: "user{}@fl.com".format(n))
