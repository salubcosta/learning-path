from django.shortcuts import render
from .models import Agenda

def listar_contato(request):
    agenda = Agenda.objects.all()
    return render(request, 'agenda/listar.html', {'contatos': agenda})