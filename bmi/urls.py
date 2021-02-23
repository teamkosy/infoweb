from django.urls import path

from . import views

urlpatterns = [
    path('', views.bmi),
    path('bmiOk', views.bmiOk),
]