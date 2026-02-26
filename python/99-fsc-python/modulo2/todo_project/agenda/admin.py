from django.contrib import admin
from .models import Agenda

@admin.register(Agenda)
class Agenda(admin.ModelAdmin):
    list_display = ['nome', 'contato', 'criado_em']
    search_fields = ['nome']
