from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('login', views.login, name='login'),
    path('doar/', views.receber_dados, name='doar'),
    path('receba/', views.receber_doacao, name='receba'),
    path('listar', views.listar_doacao, name='listar_clientes'),
    path('contato/',views.contatar,name='contato'),
]
