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
    date_created = models.DateTimeField('date created', auto_now_add=True)
    title = models.CharField("Title", 
                             name='title',
                             max_length=24)

    def __str__(self):
        return self.title

    def percent(self):
        total_rated_query = Rating.objects.filter(meal__pk=self.pk)
        total = float(total_rated_query.count())
        liked = float(total_rated_query.filter(like=True).count())
        try:
            percentage = int(liked / total)
        except ZeroDivisionError:
            return -1
        return percentage * 100


class RatingManager(models.Manager):
    def create_rating(self, member, meal, like):
        rating = self.create(member=member, meal=meal, like=like)
        # do something with the book
        return rating


class Rating(models.Model):
    """Model for rating"""
    member = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='rating')
    meal = models.ForeignKey('Meal',
                             related_name='rating')
    # True = like, False = Dislike
    like = models.BooleanField()

    objects = RatingManager()

    def __str__(self):
        return '{} - {} - {}'.format(self.meal.title, self.member.username, self.like)


class Comment(models.Model):
    """Model for a comment"""
    meal = models.ForeignKey('Meal', related_name='comment')
    message = models.TextField()
    
