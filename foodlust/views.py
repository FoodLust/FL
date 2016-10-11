from django.contrib.auth import views
from django.shortcuts import render
from meals.models import Meal

def home(request):
    """Create a home view."""
    query= Meal.photo.all()
    background_image = query.order_by('?').first()
    content = {'picture': background_image}
    return render(request, 'foodlust/home_page.html', content)