from django.shortcuts import render
import requests
import json

def movie(request):
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f9e46ed8e2b842376cd516c304c7fde2&targetDt=20201107'
    response = requests.get(url)
    response.status_code

    data = response.json()

    r_list = []
    for i in range(0, 10):
        # print(i)
        j = data['boxOfficeResult']['dailyBoxOfficeList'][i]['movieNm']
        r_list.append(j)

    open_list = []
    for i in range(0, 10):
        # print(i)
        j = data['boxOfficeResult']['dailyBoxOfficeList'][i]['openDt']
        open_list.append(j)

    audiAcc_list = []
    for i in range(0, 10):
        # print(i)
        j = data['boxOfficeResult']['dailyBoxOfficeList'][i]['audiAcc']
        audiAcc_list.append(j)

    audiAcc_list = [int(i) for i in audiAcc_list]

    total = []
    for i in range(0, 10):
        j = [r_list[i], open_list[i], audiAcc_list[i]]
        total.append(j)

    return render(request, 'infoweb/movie.html', {'total':total})
