from django.shortcuts import render, get_object_or_404
from .models import Message

def mini(request):
    msglist = Message.objects.order_by('-regdate')

    return render(request, 'infoweb/mini.html', {'msglist' : msglist})

def msgview(request):
    # msg = get_object_or_404(Message, pk=message_id)

    return render(request, 'infoweb/msgview.html')

def write(request):
    return render(request, 'infoweb/msgwrite.html')

def writeOk(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        name = request.POST.get('name')
        contents = request.POST.get('contents')

        Message.save(title,name,contents)
        msglist = Message.objects.order_by('-regdate')

        return render(request, 'infoweb/mini.html', {'msglist' : msglist})
