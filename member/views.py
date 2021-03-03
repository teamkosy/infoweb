from django.shortcuts import render

def member(request):
    return render(request,'infoweb/member.html')

def join(request):
    return render(request,'infoweb/join.html')

def joinOk(request):
    return render(request,'infoweb/index.html')