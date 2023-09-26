from django.shortcuts import render

# Create your views here.
def hello(request, name):
    message = f'반갑습니다 {name}이시여'
    return render(request, 'user_input/hello.html', {
        'message': message,
    })

def ping(request):
    return render(request, 'user_input/ping.html')

def pong(request):
    username = request.GET['username']
    password = request.GET['password']
    return render(request, 'user_input/pong.html', {
        'username': username,
        'password': password,
    })

def fibo(request):
    return render(request, 'user_input/fibo.html')


def fibo_calc(request):

    fibo_calcs = [1, 1]
    fibo_range = int(request.GET['fibo'])

    for _ in range(fibo_range):
        x, y = fibo_calcs[-1], fibo_calcs[-2]
        fibo_calcs.append(x + y)
    return render(request, 'user_input/fibo_calc.html', {
        'fibo_calcs': fibo_calcs,
    })
