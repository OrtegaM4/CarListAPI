from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, include
from CarAPI import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^cars/$', views.CarsList.as_view()),
    url(r'^cars/(?P<pk>[0-9]+)/$', views.CarsDetail.as_view()),
    # url(r'^users/$', views.UserList.as_view()),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
