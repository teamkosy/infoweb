from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def lotto(request):
    url = 'https://www.dhlottery.co.kr/gameResult.do'
    r = 951
    resp_list = []
    for i in range(5):
        params = {'method': 'byWin', 'drwNo': r}
        r = r - 1
        response = requests.get(url, params=params)
        resp_list.append(response.text)

    soup_list = []
    for resp in resp_list:
        soup_list.append(BeautifulSoup(resp))

    lotto_list = []
    total = []
    for soup in soup_list:
        num_win = soup.select_one('div.num.win')
        num_list = num_win.select('span.ball_645')
        num_bonus = soup.select_one('div.num.bonus')
        bonus = num_bonus.text.replace('\n', '').replace('보너스', '')

        data_list = []
        for item in num_list:
            num = item.text
            data_list.append(num)
            for b in bonus:
                total = (data_list, b)
        lotto_list.append(tuple(total))

    text = response.text
    soup = BeautifulSoup(text)

    num_win = soup.select_one('div.num.win')
    num_list = num_win.select('span.ball_645')
    num_bonus = soup.select_one('div.num.bonus')
    # bonus = num_bonus.select('span.ball_645')
    bonus = num_bonus.text.replace('\n', '').replace('보너스', '')

    data_list = []
    for item in num_list:
        num = item.text
        data_list.append(num)

    print(data_list, '+', bonus)

    return render(request, 'infoweb/lotto.html', context={'lotto': data_list, 'bonus':bonus})
