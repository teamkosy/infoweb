from django.urls import path

from . import views

urlpatterns = [
    path('', views.member, name='member'),
    path('memlist/', views.memlist, name='memlist'),
    path('joinOk', views.joinOk, name='joinOk'),
]