from django.urls import path
from . import views

urlpatterns = [
    path('', views.mytube, name='mytube'),
    path('new', views.video_new, name='new'),
    path('<int:video_id>', views.video_detail, name='detail'),

]