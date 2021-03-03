from django.urls import path

from . import views

urlpatterns = [
    path('', views.movie, name='movie'),
]