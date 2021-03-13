from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import JoinForm, LoginForm
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

def member(request):

    return render(request,'infoweb/login.html')


def mypage(request):

    return render(request,'infoweb/mypage.html')

def memlist(request):
    memlist = User.objects.order_by('-regdate')

    return render(request,'infoweb/memlist.html', {'memlist':memlist})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('uid')
        password = request.POST.get('upw')
        print(username, password)

        if len(username) == 0 or len(password) == 0:
            print(username, password)
            messages.add_message(request, messages.ERROR, 'ID,PW를 정확히 입력해주세요!!')
            return render(request, 'infoweb/login.html')

        else:
            uid = User.objects.get(username = username)

            if uid is not None:
                auth_login(request, uid)
                messages.add_message(request, messages.SUCCESS, '로그인 되었습니다~')
                print('로그인 성공')
                print(uid.id,uid.username)
                request.session['user_id'] = uid.id
                request.session['user_username'] = uid.username
                return render(request, 'infoweb/login.html')
            else:
                messages.add_message(request, messages.ERROR, 'ID,PW를 정확히 입력해주세요!!')
                print('로그인 실패')
        return render(request, 'infoweb/login.html')

# def loginOk(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username = username, password = password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return HttpResponse('로그인 실패. 다시 시도 해보세요.')
#     else:
#         form = LoginForm()
#         return render(request, 'infoweb/login.html', {'form': form})


def logOut(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, '로그아웃 되었습니다!!')
    return render(request, 'infoweb/login.html')

def join(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '가입되었습니다~')

            return render(request, 'infoweb/login.html')
    else:
        form = JoinForm()
        messages.add_message(request, messages.ERROR, '정보를 입력해주세요!!')
    return render(request, 'infoweb/join.html', {'form':form})


def mem_del(request):
    if request.method == 'POST':
        sid = request.POST['sid']
        User.objects.get(id=sid).delete()
        logout(request)
        a = (request.method)
        return render(request, 'infoweb/login.html', {'a':a})
    else:
        return render(request, 'infoweb/login.html', {'text':'탈퇴 실패'})