from django.db import models

# Create your models here.
class Agenda(models.Model):
    nome = models.CharField(max_length=200, blank=False)
    contato = models.CharField(max_length=11)
    observacao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

