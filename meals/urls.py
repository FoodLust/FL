from django.conf.urls import url
from .views import UploadMealView, MealDetailView, MealListView, meal_view_liked


urlpatterns = [
    url(r'^upload/$',
        UploadMealView.as_view(),
        name='upload_meal'
        ),

    url(r'^(?P<meal_pk>[0-9-]+)/liked/$',
        meal_view_liked,
        name='meal-liked',
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
