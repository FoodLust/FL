from django.conf.urls import url
from .views import UploadMealView, MealDetailView, MealListView, meal_liked, meal_disliked


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
]
