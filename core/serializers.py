from .models import Candidato
from rest_framework import serializers

class CandidatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidato
        fields = ('nome', 'foto', 'legenda', 'nascimento', 'formacao', 'renda_declarada', 'posicionamento')

