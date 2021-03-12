from django.urls import path

from . import views

urlpatterns = [
    path('', views.member, name='member'),
    path('mypage', views.mypage, name='mypage'),
    path('memlist', views.memlist, name='memlist'),
    path('loginOk', views.loginOk, name='loginOk'),
    path('joinOk', views.joinOk, name='joinOk'),
    path('logOut', views.logOut, name='logOut'),
]