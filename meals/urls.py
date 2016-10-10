from django.conf.urls import url
from .views import UploadMealView


urlpatterns = [
    url(r'^upload/$',
        UploadMealView.as_view(),
        name='upload_meal'
        )
]
