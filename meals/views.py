from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from .models import Meal, Rating, RatingManager
from members.models import Member


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
    template_name = 'meals/meal_detail.html'
    model = Meal


class MealListView(ListView):
    template_name = 'meals/meals.html'
    model = Meal
    ordering = '-date_created'


class MealListViewByRating(ListView):
    template_name = 'meals/meals_by_rating.html'
    model = Meal

    def get_context_data(self, **kwargs):
        supered = super(MealListViewByRating, self).get_context_data(**kwargs)
        sorted_supered = sorted(supered['object_list'], key=lambda meal: meal.percent(), reverse=True)
        supered['object_list'] = sorted_supered
        return supered


class MealListViewByUser(ListView):
    template_name = 'meals/meals_by_user.html'
    model = Meal
    queryset = Meal.objects.filter(meal__member__username=username)


def meal_liked(request, meal_pk):
    meal_pk = int(meal_pk)
    meal = Meal.objects.get(pk=meal_pk)
    like = True
    member = request.user

    try:
        rating = Rating.objects.get(member=member, meal=meal)
    except ObjectDoesNotExist:
        Rating.objects.create_rating(member, meal, like)
        return redirect('meals')

    rating.like = like
    rating.save()
    return redirect('meals')


def meal_disliked(request, meal_pk):
    meal_pk = int(meal_pk)
    meal = Meal.objects.get(pk=meal_pk)
    like = False
    member = request.user

    try:
        rating = Rating.objects.get(member=member, meal=meal)
    except ObjectDoesNotExist:
        Rating.objects.create_rating(member, meal, like)
        return redirect('meals')

    rating.like = like
    rating.save()
    return redirect('meals')
