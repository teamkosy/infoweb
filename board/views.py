from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .forms import MsgForm

def board(request):
    msglist = Message.objects.order_by('-regdate')

    return render(request, 'infoweb/board.html', {'msglist' : msglist})

def board_detail(request, pk):
    msg = get_object_or_404(Message, pk=pk)

    return render(request, 'infoweb/msgView.html', {'msg':msg})

# def board_del(request, pk):
#     msg = Message.objects.get(pk=pk)
#     msg.delete()
#
#     return render(request, 'infoweb/board.html')


def board_create(request):
    if request.method == 'POST':
        form = MsgForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('board')

    else:
        form = MsgForm()
    return render(request, 'infoweb/msgWrite.html', {'form':form})

