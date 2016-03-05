from django.shortcuts import render
from rest_framework import viewsets
from .models import Candidato
from .serializers import CandidatoSerializer

# Create your views here.
class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer
