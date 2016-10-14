from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from .models import Meal, Rating, RatingManager, Comment
from members.models import Member
from django.http import HttpResponse


def get_meals_user_liked(username):
    meals_user_liked = []
    user_liked = Rating.objects.filter(member__username=username, like=True)
    for ratting in user_liked:
        meals_user_liked.append(ratting.meal)
    return meals_user_liked


def get_meals_user_disliked(username):
    meals_user_disliked = []
    user_disliked = Rating.objects.filter(member__username=username, like=False)
    for ratting in user_disliked:
        meals_user_disliked.append(ratting.meal)
    return meals_user_disliked


@method_decorator(login_required, name='dispatch')
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

    def get_context_data(self, **kwargs):
        context_data = super(MealDetailView, self).get_context_data(**kwargs)
        username = self.request.user.username
        user_rating = Rating.objects.filter(member__username=username, meal=self.object).first()
        context_data['user_rating'] = user_rating
        qs = Comment.objects.filter(meal_id=context_data['meal'].id)
        context_data['comments'] = qs
        # import pdb; pdb.set_trace()
        return context_data


class MealListView(ListView):
    template_name = 'meals/meals.html'
    model = Meal
    ordering = '-date_created'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        context_data = super(MealListView, self).get_context_data(**kwargs)
        context_data['heading'] = 'Newest meals'
        username = self.request.user.username
        context_data['meals_user_liked'] = get_meals_user_liked(username)
        context_data['meals_user_disliked'] = get_meals_user_disliked(username)
        return context_data


class MealListViewTopRated(ListView):
    template_name = 'meals/meals.html'
    model = Meal
    paginate_by = 24

    def get_context_data(self, **kwargs):
        context_data = super(MealListViewTopRated, self).get_context_data(**kwargs)
        sorted_context_data = sorted(context_data['object_list'], key=lambda meal: meal.percent(), reverse=True)
        context_data['object_list'] = sorted_context_data
        context_data['heading'] = 'Top rated meals'
        username = self.request.user.username
        context_data['meals_user_liked'] = get_meals_user_liked(username)
        context_data['meals_user_disliked'] = get_meals_user_disliked(username)
        return context_data


class MealListViewByUser(ListView):
    template_name = 'meals/meals.html'
    model = Meal
    ordering = '-date_created'
    paginate_by = 24

    def get_queryset(self, **kwargs):
        username = self.request.path.split('/')[2]
        query = Meal.objects.filter(member__username=username)
        return query

    def get_context_data(self, **kwargs):
        context_data = super(MealListViewByUser, self).get_context_data(**kwargs)
        meals_by_username = self.request.path.split('/')[2]
        context_data['heading'] = 'Meals by {}'.format(meals_by_username)
        context_data['to_follow'] = meals_by_username
        username = self.request.user.username
        context_data['meals_user_liked'] = get_meals_user_liked(username)
        context_data['meals_user_disliked'] = get_meals_user_disliked(username)
        return context_data


@method_decorator(login_required, name='dispatch')
class MealListMyMeals(ListView):
    template_name = 'meals/meals.html'
    model = Meal
    ordering = '-date_created'
    paginate_by = 24

    def get_queryset(self, **kwargs):
        username = self.request.user.username
        query = Meal.objects.filter(member__username=username)
        return query

    def get_context_data(self, **kwargs):
        context_data = super(MealListMyMeals, self).get_context_data(**kwargs)
        context_data['heading'] = 'My meals'
        username = self.request.user.username
        context_data['meals_user_liked'] = get_meals_user_liked(username)
        context_data['meals_user_disliked'] = get_meals_user_disliked(username)
        return context_data


@login_required
def meal_liked(request, meal_pk):
    meal_pk = int(meal_pk)
    meal = Meal.objects.get(pk=meal_pk)
    like = True
    member = request.user

    try:
        rating = Rating.objects.get(member=member, meal=meal)
        r_percent = meal.percent()
    except ObjectDoesNotExist:
        Rating.objects.create_rating(member, meal, like)
        r_percent = meal.percent()
        return HttpResponse(r_percent)

    rating.like = like
    rating.save()
    r_percent = meal.percent()
    return HttpResponse(r_percent)


@login_required
def meal_disliked(request, meal_pk):
    meal_pk = int(meal_pk)
    meal = Meal.objects.get(pk=meal_pk)
    like = False
    member = request.user

    try:
        rating = Rating.objects.get(member=member, meal=meal)
        r_percent = meal.percent()
    except ObjectDoesNotExist:
        Rating.objects.create_rating(member, meal, like)
        r_percent = meal.percent()

    rating.like = like
    rating.save()
    r_percent = meal.percent()
    return HttpResponse(r_percent)


@login_required
def follow(request, usertofollow):
    to_follow = Member.objects.get(user__username=usertofollow)
    user = Member.objects.get(user=request.user)
    user.following.add(to_follow)
    user.save()
    return redirect('meals_by_user', username=usertofollow)


@login_required
def unfollow(request, usertostopfollow):
    stop_follow = Member.objects.get(user__username=usertostopfollow)
    user = Member.objects.get(user=request.user)
    # import pdb; pdb.set_trace()
    user.following.remove(stop_follow)
    user.save()
    return redirect('member')
