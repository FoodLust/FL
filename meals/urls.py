from django.conf.urls import url
from .views import UploadMealView, MealView, RatingView


urlpatterns = [
    url(r'^upload/$',
        UploadMealView.as_view(),
        name='upload_meal'
        ),
    url(r'^rating/(?P<pk>[0-9]+)$',
        RatingView.as_view(),
        name='detail_rating'
        ),

    url(r'^(?P<username>[A-Za-z0-9-@.+_]+)/(?P<pk>[0-9-]+)$',
        MealView.as_view(),
        name='meal'
        ),

    # url(r'^rating/new',
    #     CreateRatingView.as_view(),
    #     name='rating'
    #     )

]
