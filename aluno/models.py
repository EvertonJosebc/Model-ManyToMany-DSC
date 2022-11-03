from django.db import models
from django.forms import CharField

class Aluno(models.Model):
    nome = models.CharField(max_length = 50)
    matricula = models.CharField(max_length = 50)
    email = models.EmailField()
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
    
class Disciplina(models.Model):
    nome = models.CharField(max_length= 50)
    turno = models.CharField(max_length= 50)
    aluno = models.ManyToManyField(Aluno, through = 'AlunoDisciplina')

    def __str__(self):
        return self.nome

class AlunoDisciplina(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete = models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE)


