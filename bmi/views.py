from django.shortcuts import render

def bmi(request):
    return render(request, 'infoweb/bmi.html')

def bmiOk(request):
    if request.method == 'POST':

        w1 = request.POST.get('w')
        h1 = request.POST.get('h')

        if len(w1) == 0 or len(h1) == 0:
            # flash('측정 값을 입력하세요.')
            return render(request, 'infoweb/index.html')
        else:
            w = int(w1)
            h = int(h1)
            bmi = w / (h / 100) ** 2

            if bmi < 18.5:
                return render(request,'infoweb/bmi.html', context={'bmi' : "저체중 : 마른편입니다. 조금 더 먹어도 괜찮아요^^"})
            if bmi < 25:
                return render(request,'infoweb/bmi.html', context={'bmi' : "정상 :적당하네요^^ 잘 유지하세요~"})
            return render(request,'infoweb/bmi.html', context={'bmi' : "비만 ㅠㅠ : 다이어트가 필요합니다~"})