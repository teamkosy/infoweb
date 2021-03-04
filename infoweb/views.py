from django.shortcuts import render


def index(request):
    return render(request, 'infoweb/index.html')
