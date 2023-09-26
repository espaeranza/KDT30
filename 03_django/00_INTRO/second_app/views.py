from django.shortcuts import render

from datetime import datetime

# Create your views here.
def fibo(request):

    fibo_numbers = [1, 1]

    for _ in range(8):
        x, y = fibo_numbers[-1], fibo_numbers[-2]
        fibo_numbers.append(x + y)
    return render(request, 'fibo.html', {
        'fibo_numbers': fibo_numbers,
    })

def is_xmas(request):
    today = datetime.now()
    checker = datetime(2023, 12, 25)

    if today.month == checker.month and today.day == checker.day:
        result = '크리스마스입니다'
    else:
        result = '크리스마스가 아닙니다'
    return render(request, 'is_xmas.html', {
        'result': result,
    })