from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def news(request):
    url = 'https://news.daum.net/'
    response = requests.get(url, verify=False)
    text = response.text
    soup = BeautifulSoup(text, 'html.parser')

    title = soup.select_one('h3.tit_news').text # 기사 분류 타이틀

    # top5 기사
    data_list = []
    news1 = soup.select_one('#mArticle > div.box_peruse > div > ol > li:nth-child(1)')
    data = news1.text.replace('\n', '').replace(' ', '').replace('\'', '')
    data_list.append(data)
    news2 = soup.select_one('#mArticle > div.box_peruse > div > ol > li:nth-child(2)')
    data = news2.text.replace('\n', '').replace(' ', '').replace('\'', '')
    data_list.append(data)
    news3 = soup.select_one('#mArticle > div.box_peruse > div > ol > li:nth-child(3)')
    data = news3.text.replace('\n', '').replace(' ', '').replace('\'', '')
    data_list.append(data)
    news4 = soup.select_one('#mArticle > div.box_peruse > div > ol > li:nth-child(4)')
    data = news4.text.replace('\n', '').replace(' ', '').replace('\'', '')
    data_list.append(data)
    news5 = soup.select_one('#mArticle > div.box_peruse > div > ol > li:nth-child(5)')
    data = news5.text.replace('\n', '').replace(' ', '').replace('\'', '')
    data_list.append(data)

    #기사 링크
    link_list = []
    for i in soup.find('ol', class_='list_popcmt').find_all('li'):
        link_list.append(i.find("a")["href"])

    return render(request, 'infoweb/news.html', context={'title':title, 'data_list': data_list, 'link_list':link_list})
