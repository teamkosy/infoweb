from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .forms import MsgForm

def board(request):
    msglist = Message.objects.order_by('-regdate')

    return render(request, 'infoweb/board.html', {'msglist' : msglist})

def board_detail(request, pk):
    msg = get_object_or_404(Message, pk=pk)

    return render(request, 'infoweb/msgView.html', {'msg':msg})

def board_del(request):
    if request.method == 'POST':
        bid = request.POST['board_id']
        print(bid)
        msg = Message.objects.get(pk=bid)
        msg.delete()

        return redirect('board')
    else:
        print("실패")
        return redirect('board')


def board_create(request):
    if request.method == 'POST':
        form = MsgForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('board')
    else:
        form = MsgForm()
    return render(request, 'infoweb/msgWrite.html', {'form':form})


def board_modify(request):
    if request.method == 'POST':
        bid = request.POST.get('board_id')
        title = request.POST.get('title')
        name = request.POST.get('name')
        contents = request.POST.get('contents')
        # print(bid,title,name, contents)
        msg = Message.objects.get(pk=bid)
        msg.title = title
        msg.name = name
        msg.contents = contents
        msg.save()

        return redirect('board')

