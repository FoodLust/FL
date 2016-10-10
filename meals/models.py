from django.db import models

# Create your models here.

def upload_directory_path(instance, filename):
    return '{}/{}/{}'.format(
        instance.username,
        'meals',
        filename,
        )


class Meal(models.Model):
    """Model for a meal."""
    member = models.ForgienKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='meal',
                               related_query_name=',meal')
    photo = models.ImageField(upload_directory_path)