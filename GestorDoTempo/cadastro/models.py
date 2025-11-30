from django.db import models

# Create your models here.

DIAS_SEMANA = [
    (1, "Segunda"),
    (2, "Terça"),
    (3, "Quarta"),
    (4, "Quinta"),
    (5, "Sexta"),
]


#Classes de controle de professores 
class Professor(models.Model):
    nome = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    cor = models.CharField(max_length=20)
    dias_proibidos =  models.ManyToManyField('DiaTempoPermitido')

    def __str__(self):
        return f"{self.nome} ({self.abreviatura})" 



class Curso(models.Model):
    nome = models.CharField(max_length=100)
    periodos = models.PositiveIntegerField()
    abreviatura = models.CharField(max_length=20)
    def __str__(self):
        return self.nome

class Disciplinas(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)

    nome = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=20)
    quantidade_aulas = models.PositiveIntegerField()
    horas_aula = models.PositiveIntegerField()
    horas_relogio = models.PositiveIntegerField()
    cor = models.CharField(max_length=20)  # exemplo: #FF0000 ou "azul"
    def __str__(self):
        return self.nome

class Tempo(models.Model):
    numero = models.PositiveIntegerField()
    posicao = models.PositiveIntegerField()
    nome = models.CharField(max_length=20)
    inicio = models.TimeField()
    fim = models.TimeField()

    class Meta:
        ordering = ['posicao']

    def __str__(self):
        return f"{self.nome} : tempo {self.inicio}-{self.fim}"

class DiaSemana(models.Model):
    nome = models.CharField(max_length=20)
    posicao = models.PositiveIntegerField()
    tempos = models.ManyToManyField(Tempo)
    def __str__(self):
        return self.nome

class DiaTempoPermitido(models.Model):
    dia = models.ForeignKey(DiaSemana, on_delete=models.CASCADE)
    tempo = models.ForeignKey(Tempo, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.dia} : tempo {self.tempo}"


class Aula(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    tempo = models.ForeignKey(Tempo, on_delete=models.CASCADE, null=True, blank=True)    
    sala = models.ForeignKey('Sala', on_delete=models.CASCADE)
    dia = models.PositiveIntegerField(null=True, blank=True)
    horarios = models.ManyToManyField('DiaTempoPermitido', blank=True)
    def __str__(self):
        return f"{self.disciplina.abreviatura} ({self.disciplina.quantidade_aulas}) : {self.professor.abreviatura} : {self.sala.nome}"



class Turma(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=100)
    periodo = models.CharField(max_length=20)
    abreviatura = models.CharField(max_length=20)
    cor = models.CharField(max_length=20)  # exemplo: #FF0000 ou "azul"
    aulas = models.ManyToManyField(Aula)
    dias = models.ManyToManyField('DiaTempoPermitido')
    def __str__(self):
        return self.nome



class Semestre(models.Model):
    nome = models.CharField(max_length=100)
    periodo = models.CharField(max_length=20)
    abreviatura = models.CharField(max_length=20)    
    turmas = models.ManyToManyField(Turma)
    def __str__(self):
        return self.nome



 #################Local
class Predio(models.Model):
    nome = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=20)
    Endereco = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Sala(models.Model):
    predio = models.ForeignKey(Predio, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    descricao = models.TextField(null=True, blank=True)
    capacidade = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.nome
