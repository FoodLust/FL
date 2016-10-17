from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.dispatch import receiver


class MemberManager(models.Manager):
    """Manage the member model"""
    class Meta:
        model = 'Member'

    def get_queryset(self):
        qs = super(MemberManager, self).get_query_set()
        return qs.filter(user__is_active=True)


@python_2_unicode_compatible
class Member(models.Model):
    """ Model for members of the site """
    objects = models.Manager()

    active = MemberManager()

    user = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.deletion.CASCADE,
        related_name='member',
        unique=True
    )

    following = models.ManyToManyField('self',
                                       related_name='followers',
                                       related_query_name='followers',
                                       blank=True,
                                       default='',
                                       symmetrical=False
                                       )

    def __str__(self):
        """return the full name or username of the member"""
        fn = self.user.get_full_name().strip() or self.user.get_username()
        return '{}'.format(fn)

    @property
    def active(self):
        """get active user"""
        return self.user.is_active


@receiver(models.signals.post_save, sender=User)
def create_member(sender, **kwargs):
    """Creats a new member"""
    try:
        if kwargs.get('created', True):
            Member(user=kwargs['instance']).save()
    except ReferenceError:
        raise ReferenceError('User not in database.')
