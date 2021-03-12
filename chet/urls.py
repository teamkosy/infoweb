from django.urls import path

from . import views

urlpatterns = [
    path('', views.chet, name='chet'),
    path('chattrain', views.chattrain, name='chattrain'),
    path('chatanswer', views.chatanswer, name='chatanswer'),
]