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
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
# import infoweb.views
# import news.views
# import mini.views
# import oil.views
# import weather.views
# import lotto.views
# import bmi.views
# import movie.views
# import chet.views
# import member.views

# urlpatterns = [
#     path('', infoweb.views.index, name='home'),
#     path('news/', news.views.news, name='news'),
#     path('oil/', oil.views.oil, name='oil'),
#     path('lotto/', lotto.views.lotto, name='lotto'),
#     path('weather/', weather.views.weather, name='weather'),
#     path('movie/', movie.views.movie, name='movie'),
#     path('bmi/', bmi.views.bmi,name='bmi'),
#     # path('bmiOk/', bmi.views.bmiOk, name='bmiOk'),
#     path('mini/', mini.views.mini, name='mini'),
#     # path('mini/', Mini.as_view(), name='mini'),
#     path('msgView/<int:pk>', mini.views.msgView, name='view'),
#     path('mwrite/', mini.views.write, name='write'),
#     path('writeOk/', mini.views.writeOk, name='writeOk'),
#     path('chet/', chet.views.chet, name='chet'),
#     path('member/', member.views.member, name='member'),
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    path('', include('infoweb.urls')),
    path('news/', include('news.urls')),
    path('oil/', include('oil.urls')),
    path('lotto/', include('lotto.urls')),
    path('weather/', include('weather.urls')),
    path('movie/', include('movie.urls')),
    path('bmi/', include('bmi.urls')),
    path('mini/', include('mini.urls')),
    path('chet/', include('chet.urls')),
    path('member/', include('member.urls')),
    path('admin/', admin.site.urls),
]