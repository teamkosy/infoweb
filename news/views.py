from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def news(request):
    url = 'https://news.daum.net/'
    response = requests.get(url, verify=False)
    text = response.text
    soup = BeautifulSoup(text)
    news = soup.select_one('ol.list_popcmt')
    newslist = news.text.replace('\n', '').replace(' ', '')
    print(newslist)
    return render(request, 'infoweb/news.html', context={'newslist': newslist})
