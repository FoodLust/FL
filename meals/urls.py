from django.conf.urls import url
from .views import UploadMealView, MealDetailView, MealListView, meal_liked, \
    meal_disliked, MealListViewTopRated, MealListViewByUser, MealListMyMeals, \
    follow


urlpatterns = [
    url(r'^upload/$',
        UploadMealView.as_view(),
        name='upload_meal'
        ),

    url(r'^(?P<meal_pk>[0-9-]+)/liked/$',
        meal_liked,
        name='meal-liked',
        ),

    url(r'^(?P<meal_pk>[0-9-]+)/disliked/$',
        meal_disliked,
        name='meal-disliked',
        ),

    url(r'^(?P<pk>[0-9-]+)$',
        MealDetailView.as_view(),
        name='meal'
        ),

    url(r'^$',
        MealListView.as_view(),
        name='meals'
        ),

    url(r'^top_rated/$',
        MealListViewTopRated.as_view(),
        name='meals_top_rated'
        ),

    url(r'^my_meals/$',
        MealListMyMeals.as_view(),
        name='my_meals'
        ),

    url(r'^follow/(?P<usertofollow>[A-Za-z0-9-@._+]*)/$',
        follow,
        name='follow_user'
        ),

    # This should go last becasue it has an inclusive regular expression
    url(r'^(?P<username>[A-Za-z0-9-@._+]*)/$',
        MealListViewByUser.as_view(),
        name='meals_by_user'
        ),

]
