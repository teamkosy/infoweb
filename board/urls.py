from django.urls import path

from . import views

urlpatterns = [
    path('', views.board, name='board'),
    path('msg_write', views.msg_create, name='msg_write'),
    path('<int:pk>', views.msg_detail, name='msg_detail'),
    path('msg_del', views.msg_del, name='msg_del'),
    path('msg_modify', views.msg_modify, name='msg_modify'),
]