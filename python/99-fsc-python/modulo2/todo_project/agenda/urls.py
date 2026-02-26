from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_contato, name='listar_contatos')
]