from django.shortcuts import render
from .models import Message

def mini(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    msglist = Message.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다
    return render(request, 'infoweb/mini.html', {'msglist' : msglist})
