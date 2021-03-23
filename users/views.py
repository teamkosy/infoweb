from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import JoinForm, LoginForm, UpdateForm
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def user(request):
    return render(request,'infoweb/login.html')


def mypage(request):
    return render(request,'infoweb/mypage.html')


def userlist(request):
    userlist = User.objects.exclude(username='admin').order_by('-regdate')

    return render(request,'infoweb/userlist.html', {'userlist':userlist})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('uid')
        password = request.POST.get('upw')

        if len(username) == 0 or len(password) == 0:
            messages.add_message(request, messages.ERROR, 'ID,PW를 입력해주세요!!')
            return render(request, 'infoweb/login.html')
        else:
            user = authenticate(username = username, password = password)

            try:
                if user is not None:
                    auth_login(request, user)
                    messages.add_message(request, messages.SUCCESS, '로그인 되었습니다~')
                    print('로그인 성공')
                    request.session['user_id'] = user.id
                    request.session['user_username'] = user.username
                else:
                    messages.add_message(request, messages.ERROR, 'ID나 PW가 틀렸습니다!!')
                    print('로그인 실패')

            except Exception as ex:
                print('에러가 발생 했습니다', ex)

    return render(request, 'infoweb/login.html')


def logOut(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, '로그아웃 되었습니다!!')
    return render(request, 'infoweb/login.html')


def join(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            lname = form.cleaned_data['last_name']
            fname = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            user = User.objects.create_user(username,email,password)
            user.last_name = lname
            user.first_name = fname
            user.phone = phone
            user.save()

            messages.add_message(request, messages.SUCCESS, '가입되었습니다~')

            return render(request, 'infoweb/login.html')
    else:
        form = JoinForm()
        messages.add_message(request, messages.ERROR, '정보를 입력해주세요!!')
    return render(request, 'infoweb/join.html', {'form':form})


def user_del(request):
    if request.method == 'POST':
        sid = request.POST['sid']
        User.objects.get(id=sid).delete()
        logout(request)
        return render(request, 'infoweb/login.html')


def user_modify(request):
    if request.method == 'POST':
        id = request.POST['uid']
        # upw = request.POST['upw']
        lname = request.POST['lastname']
        fname = request.POST['firstname']
        email = request.POST['email']
        phone = request.POST['phone']

        user = User.objects.get(pk=id)
        # user.password = upw
        user.last_name = lname
        user.first_name = fname
        user.email = email
        user.phone = phone
        user.save()

        return render(request, 'infoweb/mypage.html')
    elif request.method == 'GET':
        id = request.session['user_id']
        user = User.objects.get(pk=id)
        return render(request, 'infoweb/usermodify.html', {'user':user})


def pw_modify(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, '비밀번호가 변경되었습니다~!')
            return redirect('mypage')
        else:
            messages.error(request, '비밀번호를 다시 확인해주세요!!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'infoweb/pw_modify.html', {'form': form})
