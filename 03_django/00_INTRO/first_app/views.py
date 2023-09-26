from django.shortcuts import render

from django.http import HttpResponse

import random

# Create your views here.
# 1. function view
# 2. class view

def hello(request):
    return render(request, 'hello.html')

def bye(request):
    return render(request, 'bye.html')

def lotto(request):
    lotto_nums = random.sample(range(1, 46), 6)
    lotto_nums.sort()
    context = {
        'message': '부자되고싶다',
        'lotto_nums': lotto_nums,
    }
    return render(request, 'lotto.html', context)

# /lunch/ => lunch view function => 여러 메뉴들 중에 하나 뽑아서 => 사용자에게 lunch.html로 보여줌
def lunch(request):
    menus = ['신라면', '진라면', '너구리', '삼양라면', '사리곰탕', '팔도비빔면']
    menu = random.choice(menus)
    
    return render(request, 'lunch.html', {
        'menu': menu,
    })
