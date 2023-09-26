#first_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL hello/ 로 요청이 들어오면, hello 함수를 실행할거야.
    path('hello/', views.hello),
    path('bye/', views.bye),
    path('lotto/', views.lotto),
    path('lunch/', views.lunch),
]