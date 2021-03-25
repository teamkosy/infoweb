from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .forms import MsgForm
from django.contrib import messages

def board(request):
    msglist = Message.objects.order_by('-regdate')

    return render(request, 'infoweb/board.html', {'msglist' : msglist})


def msg_create(request):
    if request.method == 'POST':
        form = MsgForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('board')
    else:
        form = MsgForm()
    return render(request, 'infoweb/msgWrite.html', {'form':form})


def msg_detail(request, pk):
    msg = get_object_or_404(Message, pk=pk)

    return render(request, 'infoweb/msgView.html', {'msg':msg})


def msg_del(request):
    if request.method == 'POST':
        mid = request.POST['msg_id']
        msg = Message.objects.get(pk=mid)
        msg.delete()

    return redirect('board')


def msg_modify(request):
    if request.method == 'POST':
        mid = request.POST.get('msg_id')
        title = request.POST.get('title')
        name = request.POST.get('name')
        contents = request.POST.get('contents')

        msg = Message.objects.get(pk=mid)
        msg.title = title
        msg.name = name
        msg.contents = contents
        msg.save()

        return redirect('board')


