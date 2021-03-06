from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import JoinForm

def member(request):
    return render(request,'infoweb/login.html')

def memlist(request):
    memlist = Member.objects.order_by('-regdate')

    return render(request,'infoweb/memlist.html', {'memlist':memlist})

def loginOk(request):
    if request.method == 'GET':
        return  render(request, 'infoweb/login.html')

    elif request.method == 'POST':

        uid = request.POST.get('uid')
        upw = request.POST.get('upw')

        id = Member.objects.get('uid')
        pw = Member.objects.get('upw')

        if len(uid) == 0 or len(upw) == 0:

            return render(request, 'infoweb/login.html')
        elif uid in Member.objects.all() :

            return render(request,'infoweb/index.html')

def joinOk(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            memlist = Member.objects.order_by('-regdate')

            return render(request, 'infoweb/index.html')

    else:
        form = JoinForm()
    return render(request, 'infoweb/join.html', {'form':form})