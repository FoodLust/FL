from django.contrib import admin
from .models import Meal, Rating, Comment

admin.site.register(Meal)
admin.site.register(Rating)
admin.site.register(Comment)