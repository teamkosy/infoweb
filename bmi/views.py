from django.shortcuts import render


def bmi(request):
    if request.method == 'GET':
        return  render(request, 'infoweb/bmi.html')

    elif request.method == 'POST':

        w1 = request.POST.get('w')
        h1 = request.POST.get('h')

        if len(w1) == 0 or len(h1) == 0:
            return render(request, 'infoweb/bmi.html')
        else:
            w = int(w1)
            h = int(h1)
            bmi = w / (h / 100) ** 2

            if bmi < 18.5:
                return render(request,'infoweb/bmi.html', context={'bmi' : "저체중 : 마른편입니다. 조금 더 먹어도 괜찮아요^^", 'rs':bmi})
            if bmi < 25:
                return render(request,'infoweb/bmi.html', context={'bmi' : "정상 : 적당하네요^^ 잘 유지하세요~", 'rs':bmi})
            return render(request,'infoweb/bmi.html', context={'bmi' : "비만 ㅠㅠ : 다이어트가 필요합니다~", 'rs':bmi})