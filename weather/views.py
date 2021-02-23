from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def weather(request):
    if request.method == 'POST':

        url = 'https://weather.naver.com/today/02150101'
        response = requests.get(url)
        print(response.status_code)

        text = response.text
        soup = BeautifulSoup(text)
        temp = '현재온도 -1° 어제보다 2°낮아요 맑음 습도35% 북풍1m/s 체감-3°'

        for i in soup.select_one('div.weather_area'):
            blind = soup.select_one('div.weather_area')
            data = blind.text.replace('\n', '')

        return render(request,'infoweb/index.html', context={'data' : data, 'temp' : temp })
        print(data)