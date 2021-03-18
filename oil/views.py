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

    #휘발유
    oil1 = soup.select_one(
        '#main_pack > section.sc_new.cs_gold > div > div.api_cs_wrap.contents03 > div > div.ar_cont > div.cont_dtcon.cont_tb > div > ul:nth-child(2) > li:nth-child(1) > dl > dd > strong').text
    #경유
    oil2 = soup.select_one(
        '#main_pack > section.sc_new.cs_gold > div > div.api_cs_wrap.contents03 > div > div.ar_cont > div.cont_dtcon.cont_tb > div > ul:nth-child(2) > li:nth-child(3) > dl > dd > strong').text

    day = soup.select_one('#main_pack > section.sc_new.cs_gold > div > div.api_cs_wrap.contents03 > div > div.ar_cont > div.cont_dtcon.cont_tb > div > ul:nth-child(2) > li:nth-child(1) > dl > dt > em').text

    return render(request,'infoweb/oil.html', {'oil':oil, 'oil1':oil1, 'oil2':oil2, 'day':day})
