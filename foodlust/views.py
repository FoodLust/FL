from django.contrib.auth import views
from django.shortcuts import render
from meals.models import Meal

def home(request):
    """Create a home view."""   
    query= Meal.objects.all()
    background_image = query.order_by('?').first().photo
    content = {'picture': background_image}
    return render(request, 'foodlust/home_page.html', content)