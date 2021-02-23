from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse


def oil(request):
    return render(request,'infoweb/index.html')