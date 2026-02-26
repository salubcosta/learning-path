from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_tarefas, name='listar_tarefas'),
]