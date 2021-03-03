from django.urls import path

from . import views

urlpatterns = [
    path('', views.mini, name='mini'),
    path('write', views.write, name='write'),
    path('view/<int:message_id>', views.View.as_view(), name='view'),
    # path('view/<int:id>', views.view, name='view'),
    path('writeOk', views.writeOk, name='writeOk'),
]