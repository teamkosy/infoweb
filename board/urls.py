from django.urls import path

from . import views

urlpatterns = [
    path('', views.board, name='board'),
    path('write/', views.board_create, name='write'),
    path('<int:pk>/', views.board_detail, name='detail'),
]