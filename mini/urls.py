from django.urls import path

from . import views

urlpatterns = [
    path('', views.mini, name='mini'),
    path('write', views.write, name='write'),
    path('view/<int:pk>', views.View.as_view(), name='view'),
    path('writeOk', views.writeOk, name='writeOk'),
]