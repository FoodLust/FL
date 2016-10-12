from django.conf.urls import url
from .views import UploadMealView, MealDetailView, MealListView
# , mealViewLiked


urlpatterns = [
    url(r'^upload/$',
        UploadMealView.as_view(),
        name='upload_meal'
        ),

    # url(r'^(?P<pk>[0-9-]+)/liked$',
    #     mealViewLiked(),
    #     name='meal-liked',
    #     ),

    url(r'^(?P<pk>[0-9-]+)$',
        MealDetailView.as_view(),
        name='meal'
        ),

    url(r'^$',
        MealListView.as_view(),
        name='meals'
        ),

]
