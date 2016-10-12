from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from .models import Meal, Rating, RatingManager


# @method_decorator(login_required, name='dispatch')
class UploadMealView(CreateView):
    template_name = 'meals/uploads_meal.html'
    model = Meal
    fields = ['title', 'photo']

    def get_success_url(self):
        """Set redirection upon successful upload."""
        url = reverse('meals')
        return url

    def form_valid(self, form):
        """Modify form validation to apply a user to an instance."""
        form.instance.member = self.request.user
        return super(UploadMealView, self).form_valid(form)


class MealDetailView(DetailView):
    template_name = 'meals/meal.html'
    model = Meal


class MealListView(ListView):
    template_name = 'meals/meals.html'
    model = Meal


class RatingView(DetailView):
    template_name = 'meals/rating.html'
    model = Rating


# def mealViewLiked():
#     member = self.request.user
#     meal_id = int(self.request.path.split('/')[2])
#     meal = Meal.objects.get(pk=meal_id)
#     like = True
#     RatingManager.create_rating(member, meal, like)


# @method_decorator(login_required, name='dispatch')
# class MealViewLiked(CreateView):
#     template_name = 'meals/create_rating.html'
#     model = Rating
    # fields = ['like']
    # model.like = True

    # def form_valid(self, form):
    #     """Modify form validation to apply a user to an instance."""
    #     form.instance.member = self.request.user
    #     meal_number = int(self.request.path.split('/')[2])
    #     my_meal = Meal.objects.get(pk=meal_number)
    #     form.instance.meal = my_meal

    #     return super(MealViewLiked, self).form_valid(form)

    # def get_success_url(self):
    #     """Set redirection upon successful upload."""
    #     url = reverse('meal', args=[self.object.meal.pk])
    #     return url
