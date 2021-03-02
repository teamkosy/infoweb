from django.shortcuts import render, get_object_or_404
from .models import Message

def mini(request):
    msglist = Message.objects.all()

    return render(request, 'infoweb/mini.html', {'msglist' : msglist})

def msgview(request):
    # msg = get_object_or_404(Message, pk=message_id)

    return render(request, 'infoweb/msgview.html')

def write(request):
    return render(request, 'infoweb/msgwrite.html')

def writeOk(request):

    msglist = Message.objects.all()
    return render(request, 'infoweb/mini.html', {'msglist' : msglist})
