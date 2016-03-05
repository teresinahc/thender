from django.db import models


class Posicionamento(models.Model):
    tag = models.CharField(max_length=32)

    def __unicode__(self):
        return self.tag

class Legenda(models.Model):
    nome = models.CharField(max_length=100, blank=True)
    sigla = models.CharField(max_length=8, blank=True)

    def __unicode__(self):
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
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    class Meta:
        ordering = ('nome', 'legenda')

    def __unicode__(self):
        return self.nome

    def like(self):
        self.likes += 1
        self.save()

    def dislike(self):
        self.dislikes += 1
        self.save()
