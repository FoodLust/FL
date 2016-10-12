from django.contrib.auth.decorators import login_required
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
    template_name = 'meals/meal.html'
    model = Meal


class MealListView(ListView):
    template_name = 'meals/meals.html'
    model = Meal


class RatingView(DetailView):
    template_name = 'meals/rating.html'
    model = Rating


def meal_view_liked(request, meal_pk):
    # import pdb; pdb.set_trace()
    meal_pk = int(meal_pk)
    meal = Meal.objects.get(pk=meal_pk)
    like = True
    member = request.user
    Rating.objects.create_rating(member, meal, like)
    return redirect('meals')
