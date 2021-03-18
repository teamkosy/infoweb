"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


urlpatterns = [
    path('', include('infoweb.urls')),
    path('album/', include('album.urls')),
    path('mytube/', include('mytube.urls')),
    path('news/', include('news.urls')),
    path('oil/', include('oil.urls')),
    path('lotto/', include('lotto.urls')),
    path('weather/', include('weather.urls')),
    path('movie/', include('movie.urls')),
    path('bmi/', include('bmi.urls')),
    path('board/', include('board.urls')),
    path('chet/', include('chet.urls')),
    path('member/', include('users.urls')),
    path('admin/', admin.site.urls),
]