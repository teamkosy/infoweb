from django.shortcuts import render, get_object_or_404
from mini.models import Message
from django.views import generic

def mini(request):
    msglist = Message.objects.order_by('-regdate')

    return render(request, 'infoweb/mini.html', {'msglist' : msglist})

# def view(request, id):
#     msg = get_object_or_404(Message, pk=id)
#
#     return render(request, 'infoweb/msgView.html')

def write(request):
    return render(request, 'infoweb/msgWrite.html')

def writeOk(request):
    m = Message
    if request.method == 'POST':
        title = request.POST.get('title')
        name = request.POST.get('name')
        content = request.POST.get('content')

        m.save(title,name,content)
        msglist = Message.objects.order_by('-regdate')

        return render(request, 'infoweb/mini.html', {'msglist' : msglist})

class View(generic.DetailView):
    model = Message
    # return render(request, 'infoweb/msgView.html')
