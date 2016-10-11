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

# class CreateRatingView(CreateView):
#     template_name = 'meals/create_rating.html'
#     model = Rating
#     success_url = '/'
#     fields = ['like']


# @method_decorator(login_required, name='dispatch')
class MealViewLiked(CreateView):
    template_name = 'meals/create_rating.html'
    model = Rating
    fields = ['like']

    def form_valid(self, form):
        """Modify form validation to apply a user to an instance."""
        form.instance.member = self.request.user
        meal_number = int(self.request.path.split('/')[2])
        my_meal = Meal.objects.get(pk=meal_number)
        form.instance.meal = my_meal

        return super(MealViewLiked, self).form_valid(form)

    def get_success_url(self):
        """Set redirection upon successful upload."""
        url = reverse('meal', args=[self.object.meal.pk])
        return url
