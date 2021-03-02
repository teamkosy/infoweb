from django.urls import path

from . import views

urlpatterns = [
    path('', views.mini),
    # path('msgview/{{list.id}}', views.msgview),
    path('write', views.write),
    path('writeOk', views.writeOk),
]