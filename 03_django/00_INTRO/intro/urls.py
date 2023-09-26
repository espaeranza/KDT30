"""
URL configuration for intro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_app/', include('first_app.urls')),
    path('second_app/', include('second_app.url')),

    # second_app의 모든 패턴은 'second_app/'으로 시작
    # second_app/fibo/ 로 접속시  => view의 fibo 함수 실행
    # fibo는 피보나치 수열 10개를 fibo.html에서 사용자에게 보여줌 (ul > li)

    # second_app/is_xmas/로 접속시 => view의 is_xmas 함수 실행
    # is xmas 함수는 오늘이 크리스마스라면 yes를 아니라면 no를 is_xmas.html에서 보여줌


]


# Req => (http://127.0.0.1:8000/) hello/
# Res => 'Hello Django'