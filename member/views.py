from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import JoinForm, LoginForm
from django.contrib.auth import login as auth_login
from django.contrib import messages

def member(request):

    return render(request,'infoweb/login.html')


def memlist(request):
    memlist = Member.objects.order_by('-regdate')

    return render(request,'infoweb/memlist.html', {'memlist':memlist})


def loginOk(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '로그인 되었습니다~')

            return render(request, 'infoweb/login.html')

    else:
        form = LoginForm()
        messages.add_message(request, messages.ERROR, '정보를 입력해주세요!!')
    return render(request, 'infoweb/join.html', {'loginform': form})


def joinOk(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '가입되었습니다~')

            return render(request, 'infoweb/index.html')

    else:
        form = JoinForm()
        messages.add_message(request, messages.ERROR, '정보를 입력해주세요!!')
    return render(request, 'infoweb/join.html', {'form':form})