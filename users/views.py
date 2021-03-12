from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import JoinForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def member(request):

    return render(request,'infoweb/login.html')


def mypage(request):

    return render(request,'infoweb/mypage.html')

def memlist(request):
    memlist = User.objects.order_by('-regdate')

    return render(request,'infoweb/memlist.html', {'memlist':memlist})


def loginOk(request):
    if request.method == 'POST':
        username = request.POST.get('uid')
        password = request.POST.get('upw')
        print(username, password)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, '로그인 되었습니다~')
            print('로그인 성공')
            return redirect('home')

        else:
            messages.add_message(request, messages.ERROR, 'ID,PW를 입력해주세요!!')
            print('로그인 실패')
    return render(request, 'infoweb/login.html')


def logOut(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, '로그아웃 되었습니다!!')
    return redirect('home')


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