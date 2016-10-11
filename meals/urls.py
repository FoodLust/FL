from django.conf.urls import url
from .views import UploadMealView, MealView


urlpatterns = [
    url(r'^upload/$',
        UploadMealView.as_view(),
        name='upload_meal'
        ),
    url(r'^(?P<username>[A-Za-z0-9-@.+_]*)/(?P<pk>[0-9-]*)$',
        MealView.as_view(),
        name='meal'
        )

]
