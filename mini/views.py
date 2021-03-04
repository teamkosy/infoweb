from django.shortcuts import render, get_object_or_404
from .models import Message
from .forms import MsgForm

def mini(request):
    msglist = Message.objects.order_by('-regdate')

    return render(request, 'infoweb/mini.html', {'msglist' : msglist})

def mini_detail(request, pk):
    msg = get_object_or_404(Message, pk=pk)

    return render(request, 'infoweb/msgView.html', {'msg':msg})

# def write(request):
#     return render(request, 'infoweb/msgWrite.html')


def mini_create(request):
    if request.method == 'POST':
        form = MsgForm(request.POST)
        if form.is_valid():
            form.save()
            msglist = Message.objects.order_by('-regdate')

            return render(request, 'infoweb/mini.html', {'msglist': msglist})

    else:
        form = MsgForm()
    return render(request, 'infoweb/msgWrite.html', {'form':form})

