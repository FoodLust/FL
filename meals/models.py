from django.db import models
from django.conf import settings


# Create your models here.

def upload_directory_path(instance, filename):
    return '{}/{}'.format(
        instance.username,
        filename,)


class Meal(models.Model):
    """Model for a meal."""
    member = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='meal',
                               related_query_name='meal')
    photo = models.ImageField(upload_directory_path)
    date_created = models.DateField('date created', auto_now_add=True)
    title = models.CharField("Title", 
                             name='title',
                             max_length=128)


class Ratting(models.Model):
    """Model for ratting"""
    member = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='ratting')
    meal = models.ForeignKey('Meal',
                             related_name='ratting')
    # True = like, False = Dislike
    like = models.BooleanField()
    # ratting = models.CharField(max_length=8,
    #                            choices=[('like', 'like'),
    #                                     ('dislike', 'dislike')])
