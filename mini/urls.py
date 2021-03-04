from django.urls import path

from . import views

urlpatterns = [
    path('', views.mini, name='mini'),
    path('write/', views.mini_create, name='write'),
    path('<int:pk>/', views.mini_detail, name='detail'),
    # path('view/<int:id>', views.view, name='view'),
    # path('writeOk', views.writeOk, name='writeOk'),
]