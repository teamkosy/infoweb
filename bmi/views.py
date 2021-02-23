from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse


def bmi(request):
    w1 = request.POST['w']
    h1 = request.POST['h']


    w = int(75)
    h = int(168)
    bmi = w / (h / 100) ** 2
    if bmi < 18.5:

        return render(request,'infoweb/index.html', {'bmi' : "저체중 : 마른편입니다. 조금 더 먹어도 괜찮아요^^"})
    if bmi < 25:

        return render(request,'infoweb/index.html', {'bmi' : "정상 :적당하네요^^ 잘 유지하세요~"})

    return render(request,'infoweb/index.html', {'bmi' : "비만 ㅠㅠ : 다이어트가 필요합니다~"})