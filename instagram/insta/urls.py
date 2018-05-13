from django.conf.urls import url
from . import views
from django.conf import settings


urlpatterns=[
    url('^$',views.home,name='home'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^settings/',views.settings,name='settings'),
    url(r'^edit/',views.edit,name='edit'),
    ]
