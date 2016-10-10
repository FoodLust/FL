import factory
from django.contrib.auth.models import User
from members.models import Member


class MemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Member

    username = 'bob24'
    email = 'bob24@bob.com'
