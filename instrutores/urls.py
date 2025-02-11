from django.urls import path
from . import views

app_name = 'instrutores'

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar, name='listar'),
    path('bomdia/', views.show_mensagem, name='bomdia'),
]