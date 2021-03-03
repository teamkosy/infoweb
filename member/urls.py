from django.urls import path

from . import views

urlpatterns = [
    path('', views.member, name='member'),
    path('join/', views.join, name='join'),
    path('joinOk/', views.joinOk, name='joinOk'),
]