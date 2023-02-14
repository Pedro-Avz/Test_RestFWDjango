from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    ra = models.IntegerField()
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
