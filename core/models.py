from django.db import models


class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='uploads/candidatos/',
                             blank=True, null=True)
    legenda = models.CharField(max_length=100, blank=True)
    nascimento = models.DateField()
    formacao = models.CharField(max_length=100, blank=True)
    renda_declarada = models.FloatField()
    posicionamento = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome

