from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = {
    url(r'^$', views.index),
    url(r'^recent/', views.recent),
    url(r'^news/', views.news),

}

