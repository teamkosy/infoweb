from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def index(request):
    return render(request, 'infoweb/index.html')

def news(request):
    url = 'https://news.daum.net/'
    response = requests.get(url, verify=False)
    text = response.text
    soup = BeautifulSoup(text)
    news = soup.select_one('ol.list_popcmt')
    newslist = news.text.replace('\n', '').replace(' ', '')
    print(newslist)
    return render(request, 'infoweb/index.html', context={'newslist':newslist})

def weather(request):
    url = 'https://weather.naver.com/today/02150101'
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text)
    blind = soup.select_one('div.weather_area')
    weather = blind.text.replace('\n', '').replace(' ', '')
    return render(request, 'infoweb/index.html', context={'weather':weather})
