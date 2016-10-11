from django.conf.urls import url
from .views import UploadMealView, MealView, RatingView, MealsView


urlpatterns = [
    url(r'^upload/$',
        UploadMealView.as_view(),
        name='upload_meal'
        ),
    url(r'^rating/(?P<pk>[0-9]+)$',
        RatingView.as_view(),
        name='detail_rating'
        ),

    url(r'^(?P<pk>[0-9-]+)$',
        MealView.as_view(),
        name='meal'
        ),

    url(r'^$',
        MealsView.as_view(),
        name='meals'
        ),

]
