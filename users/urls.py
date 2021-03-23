from django.urls import path

from . import views

urlpatterns = [
    path('', views.user, name='user'),
    path('mypage', views.mypage, name='mypage'),
    path('userlist', views.userlist, name='user_list'),
    path('login', views.login, name='login'),
    path('join', views.join, name='join'),
    path('logOut', views.logOut, name='logOut'),
    path('userdel', views.user_del, name='user_del'),
    path('usermodify', views.user_modify, name='user_modify'),
    path('pwmodify', views.pw_modify, name='pw_modify'),

]