"""foodlust URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from foodlust.views import home, about, home_redirect
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from members.views import member_view, edit_member_view


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^meals/', include('meals.urls')),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='auth_logout'),
    url(r'^about/', about, name='about'),
    url(r'^accounts/profile/', home_redirect),
    url(r'^member/$', member_view, name='member'),
    url(r'^member/edit$', edit_member_view, name='member_edit'),
    # url(r'^password_change/done$', auth_views.password_change_done),
    # url(r'^password_reset/done$', auth_views.password_reset_done),
    # url(r'^reset/done/$', auth_views.password_reset_complete),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm),
    # url(r'^password_reset/$', auth_views.password_reset),
    # url(r'^password_change/$', auth_views.password_change, {'template_name': 'registration/password_change_form.html'}),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
        )
