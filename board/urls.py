from django.urls import path

from . import views

urlpatterns = [
    path('', views.board, name='board'),
    path('write/', views.board_create, name='write'),
    path('<int:pk>/', views.board_detail, name='detail_view'),
    path('board_del', views.board_del, name='board_del'),
    path('board_modify', views.board_modify, name='board_modify'),
]