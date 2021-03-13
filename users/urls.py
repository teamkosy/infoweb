from django.urls import path

from . import views

urlpatterns = [
    path('', views.member, name='member'),
    path('mypage', views.mypage, name='mypage'),
    path('memlist', views.memlist, name='memlist'),
    path('login', views.login, name='login'),
    path('join', views.join, name='join'),
    path('logOut', views.logOut, name='logOut'),
]