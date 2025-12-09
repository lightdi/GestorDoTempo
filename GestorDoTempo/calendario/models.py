from django.db import models
from cadastro.models import Turma, Curso
from django.utils import timezone

# Create your models here.

class TipoEventos(models.Model):
    nome = models.CharField(max_length=200)
    cor = models.CharField(max_length=200)
    integrado = models.BooleanField(default=False)
    superior = models.BooleanField(default=False)
    def __str__(self):
        tipo = ""
        if self.integrado:
            tipo = "Integrado"
        if self.superior:
            tipo += " Superior"
        return f"{self.nome} : {tipo}" 

class Event(models.Model):
    title = models.CharField(max_length=200)
    tipo = models.ForeignKey(TipoEventos, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class EventDate(models.Model):
    event = models.ForeignKey(Event, related_name='dates', on_delete=models.CASCADE)
    date = models.DateField()
    
    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.event.title} - {self.date}"
