from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def weather(request):
    if request.method == 'POST':

        url = 'https://weather.naver.com/today/02150101'
        response = requests.get(url)
        text = response.text
        soup = BeautifulSoup(text)

        for i in soup.select_one('div.weather_area'):
            blind = soup.select_one('div.weather_area')
            weather = blind.text.replace('\n', '').replace(' ', '')
        print(data)
        return render(request,'infoweb/index.html', context={'weather' : weather })
