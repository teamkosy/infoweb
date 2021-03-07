from django.shortcuts import render
import requests

def movie(request):
    url = 'https://www.kobis.or.kr/kobis/business/main/searchMainDailyBoxOffice.do'
    response = requests.get(url)
    movie = response.json()
    date = movie[0]['startDate']

    movie_list = []
    for i in range(0, 10):
        rs = movie[i]
        a = (rs['rank'], rs['movieNm'], rs['openDt'], rs['salesAmt'], rs['audiCnt'], rs['rankInten'])
        movie_list.append(a)

    return render(request, 'infoweb/movie.html', {'movie_list':movie_list, 'date':date})