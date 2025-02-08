from django.urls import path
from . import views

app_name = 'tipodeatividade'

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar, name='listar'),
    path('consultar/', views.consultar, name='consultar'),
    path('bomdia/', views.show_mensagem, name='bomdia'),
]