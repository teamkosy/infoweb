from django.shortcuts import render
from .models import Video

def mytube(request):
    video_list = Video.objects.order_by('-update')

    return render(request, 'infoweb/video_list.html', {'video_list': video_list})

def video_new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        video_key = request.POST.get('video_key')

        if title or video_key != '':
            Video.objects.create(title=title, video_key=video_key)
            video_list = Video.objects.order_by('-update')

            return render(request, 'infoweb/video_list.html', {'video_list': video_list})
        else:
            return render(request, 'infoweb/video_new.html')


    elif request.method == 'GET':
        return render(request, 'infoweb/video_new.html')


def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)

    return render(request, 'infoweb/video_detail.html', {'video': video})

