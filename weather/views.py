from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def weather(request):
    url = 'https://weather.naver.com/today/02150101'
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text)

    blind = soup.select_one('div.weather_area')
    weather = blind.text.replace('\n', '').replace(' ', '')

    return render(request,'infoweb/weather.html', context={'weather' : weather })
