from django.db import models


class Posicionamento(models.Model):
    tag = models.CharField(max_length=32)

    def __str__(self):
        return self.tag

class Legenda(models.Model):
    nome = models.CharField(max_length=100, blank=True)
    sigla = models.CharField(max_length=8, blank=True)

    def __str__(self):
        return '%s-%s' % (self.nome, self.sigla)

class Candidato(models.Model):
    nome = models.CharField(max_length=100, db_index=True)
    foto = models.ImageField(upload_to='uploads/candidatos/',
                             blank=True, null=True)
    legenda = models.ForeignKey(Legenda)
    nascimento = models.DateField()
    formacao = models.CharField(max_length=100, blank=True)
    renda_declarada = models.FloatField()
    posicionamento = models.ManyToManyField(Posicionamento, blank=True)

    class Meta:
        ordering = ('nome', 'legenda')

    def __str__(self):
        return self.nome
