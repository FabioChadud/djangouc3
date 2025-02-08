from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listar/', views.listar, name='listar'),
    path('consulta/', views.listar, name='consulta'),
    path('bomdia/', views.show_mensagem, name='bomdia')
    
]