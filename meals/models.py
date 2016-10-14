from django.db import models
from django.conf import settings


def upload_directory_path(instance, filename):
    """Saves a meal photo to the media directory in a sub-directory named as the uploaders username"""
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
        """Return the meals title."""
        return self.title

    def percent(self):
        """Get the like percentage of a meal. If there are no ratings return -1"""
        total_rated_query = Rating.objects.filter(meal__pk=self.pk)
        total = float(total_rated_query.count())
        liked = float(total_rated_query.filter(like=True).count())
        try:
            percentage = int(liked / total)
        except ZeroDivisionError:
            return -1
        return percentage * 100


class RatingManager(models.Manager):
    """Creats a new ratting in the database"""
    def create_rating(self, member, meal, like):
        rating = self.create(member=member, meal=meal, like=like)
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
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='comment')
    date_created = models.DateTimeField('date created', auto_now_add=True)
