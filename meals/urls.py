from django.conf.urls import url
from .views import UploadMealView, MealView, MealViewLiked, MealsView


urlpatterns = [
    url(r'^upload/$',
        UploadMealView.as_view(),
        name='upload_meal'
        ),
    # url(r'^rating/(?P<pk>[0-9]+)$',
    #     RatingView.as_view(),
    #     name='detail_rating'
    #     ),
    # url(r'^rating/new',
    #     CreateRatingView.as_view(),
    #     name='create_rating'
    #     ),

    url(r'^(?P<pk>[0-9-]+)/liked$',
        MealViewLiked.as_view(),
        name='meal-liked',
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
