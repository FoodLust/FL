from django.db import models
from django.conf import settings


# Create your models here.

def upload_directory_path(instance, filename):
    return '{}/{}'.format(
        instance.member.username,
        filename,)


class Meal(models.Model):
    """Model for a meal."""
    member = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='meal',
                               related_query_name='meal')
    photo = models.ImageField(upload_to=upload_directory_path)
    date_created = models.DateField('date created', auto_now_add=True)
    title = models.CharField("Title", 
                             name='title',
                             max_length=128)

    def __str__(self):
        return self.title


class Rating(models.Model):
    """Model for rating"""
    member = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='rating')
    meal = models.ForeignKey('Meal',
                             related_name='rating')
    # True = like, False = Dislike
    like = models.BooleanField()
    # rating = models.CharField(max_length=8,
    #                            choices=[('like', 'like'),
    #                                     ('dislike', 'dislike')])

    def __str__(self):
        return '{} - {} - {}'.format(self.meal.title, self.member.username, self.like)
