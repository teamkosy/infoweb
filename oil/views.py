from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def oil(request):
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%9C%A0%EA%B0%80%EC%A0%95%EB%B3%B4'
    response = requests.get(url)

    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    row = soup.select_one('ul.lsttype_tb')
    oil = row.text.replace(' ', '')
    oil

    return render(request,'infoweb/oil.html', {'oil':oil})