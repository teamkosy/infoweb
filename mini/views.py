from django.shortcuts import render, get_object_or_404
from mini.models import Message
from django.views import generic

def mini(request):
    msglist = Message.objects.order_by('-regdate')

    return render(request, 'infoweb/mini.html', {'msglist' : msglist})

# def view(request):
#     # msg = get_object_or_404(Message, pk=message_id)
#
#     return render(request, 'infoweb/msgView.html')

def write(request):
    return render(request, 'infoweb/msgWrite.html')

def writeOk(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        name = request.POST.get('name')
        content = request.POST.get('content')

        Message.save(title,name,content)
        msglist = Message.objects.order_by('-regdate')

        return render(request, 'infoweb/mini.html', {'msglist' : msglist})

class View(generic.DetailView):
    model = Message
