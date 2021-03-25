from django.shortcuts import render
import requests

def index(request):
    url = 'https://imnews.imbc.com/js/coviddata.json'
    response = requests.get(url)
    covid = response.json()
    covid_list = list(covid.values())

    return render(request, 'infoweb/index.html', {'covid_list': covid_list})