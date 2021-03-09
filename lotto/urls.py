from django.urls import path

from . import views

urlpatterns = [
    path('', views.lotto, name='lotto'),
    path('lottonum', views.lottonum, name='lottonum'),
]