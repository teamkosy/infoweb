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
import infoweb.views
import news.views
import mini.views
import oil.views
import weather.views
import lotto.views
import bmi.views
import movie.views
# import chet.views
# import member.views

urlpatterns = [
    path('', infoweb.views.index, name='home'),
    path('news/', news.views.news, name='news'),
    path('oil/', oil.views.oil, name='oil'),
    path('lotto/', lotto.views.lotto, name='lotto'),
    path('weather/', weather.views.weather, name='weather'),
    path('movie/', movie.views.movie, name='movie'),
    path('bmi/', bmi.views.bmi,name='bmi'),
    # path('bmiOk/', bmi.views.bmiOk, name='bmiOk'),
    path('mini/', mini.views.mini, name='mini'),
    path('msgview/', mini.views.msgview, name='view'),
    path('write/', mini.views.write, name='write'),
    path('writeOk/', mini.views.writeOk, name='writeOk'),
    # path('chet/', include('chet.urls')),
    # path('member/', include('member.urls')),
    path('admin/', admin.site.urls),
]

# urlpatterns = [
#     path('', include('infoweb.urls', name='home')),
#     path('news/', include('news.urls', name='news')),
#     path('oil/', include('oil.urls', name='oil')),
#     path('lotto/', include('lotto.urls', name='lotto')),
#     path('weather/', include('weather.urls', name='weather')),
#     # path('movie/', include('movie.urls', name='movie')),
#     path('bmi/', include('bmi.urls')),
#     path('bmiOk', include('bmi.urls', name='bmiOk')),
#     path('mini/', include('mini.urls', name='mini')),
#     path('msgview/<int:message_id>/', mini.views.msgview, name='view'),
#     path('write', include('mini.urls', name='write')),
#     path('writeOk', include('mini.urls', name='writeOk')),
#     # path('chet/', include('chet.urls')),
#     # path('member/', include('member.urls')),
#     path('admin/', admin.site.urls),
# ]