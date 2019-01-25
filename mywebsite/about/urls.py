from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = {
    url(r'^profil/$', views.profil),
    url(r'^$', views.index),
}

