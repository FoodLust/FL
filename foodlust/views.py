from django.contrib.auth import views
from django.shortcuts import render, redirect
from meals.models import Meal


def home(request):
    """Create a home view."""
    return render(request, 'foodlust/home_page.html')


def about(request):
    """Create an about view."""
    return render(request, 'foodlust/about_us.html')


def home_redirect(request):
    """Redirect to the home page."""
    return redirect('home')
