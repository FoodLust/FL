from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.dispatch import receiver


@python_2_unicode_compatible
class Member(models.Model):
    """ Model for members of the site """

    objects = models.Manager()

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        on_delete=models.deletion.CASCADE,
        related_name='member',
        unique=True
    )

    def __str__(self):
        fn = self.user.get_full_name().strip() or self.user.get_username()
        return '{}'.format(fn)

    @property
    def active(self):
        return self.user.is_active
