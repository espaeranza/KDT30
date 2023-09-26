from django.urls import path
from . import views

urlpatterns = [
    path('hello/<str:name>/', views.hello),
    path('ping/', views.ping),
    path('pong/', views.pong),
    path('fibo/', views.fibo),
    path('fibo_calc/', views.fibo_calc),
]
