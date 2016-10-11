from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView
from .models import Meal, Rating

# @method_decorator(login_required, name='dispatch')
class UploadMealView(CreateView):
    template_name = 'meals/uploads_meal.html'
    model = Meal
    success_url = '/'
    fields = ['title', 'photo']

    # def get_success_url(self):
        # """Set redirection upon successful upload."""
        # url = reverse('library_view')
        # return url

    def form_valid(self, form):
        """Modify form validation to apply a user to an instance."""
        form.instance.member = self.request.user
        return super(UploadMealView, self).form_valid(form)


class MealView(DetailView):
    template_name = 'meals/meal.html'
    model = Meal

class RatingView(DetailView):
    template_name = 'meals/rating.html'
    model = Rating
