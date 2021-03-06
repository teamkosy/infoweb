from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from random import *

def lotto(request):
    url = 'https://www.dhlottery.co.kr/gameResult.do?method=byWin&wiselog=C_A_1_1'
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text)

    num_win = soup.select_one('div.num.win')
    num_list = num_win.select('span.ball_645')
    num_bonus = soup.select_one('div.num.bonus')
    bonus = num_bonus.text.replace('\n', '').replace('보너스', '')
    data = soup.select_one('h4')
    date = data.text

    data_list = []
    for item in num_list:
        num = item.text
        data_list.append(num)

    return render(request, 'infoweb/lotto.html', context={'data_list': data_list, 'bonus':bonus, 'date':date})


def lottonum(request):
    if request.method == 'POST':
        game = request.POST['game']
        if len(game) == 0:
            return render(request, 'infoweb/lottonum.html')
        else:
            gnum = int(game)
            num = range(1, 46)
            num = list(num)
            lotto_list = []

            for i in range(0, gnum):
                shuffle(num)
                lottonum = sample(num, 6)
                lottonum.sort()
                lotto_list.append([lottonum])
            return render(request, 'infoweb/lottonum.html', {'lotto_list': lotto_list})

    else:
        print('실패')

    return render(request, 'infoweb/lottonum.html')
