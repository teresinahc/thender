from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from .models import Candidato
from .serializers import CandidatoSerializer

# Create your views here.
class CandidatoViewSet(viewsets.ModelViewSet):
    """
    API endpoint para Candidatos
    """
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer

    @detail_route(methods=['post'], url_path='like')
    def like(self, request, pk=None):
        if not pk in request.session.get('likes', []):
            candidato = get_object_or_404(Candidato, pk)
            candidato.like()
            if request.session.get('likes', False):
                request.session['likes'].append(pk)
            else:
                request.session['likes'] = [pk]
            return Response({'status': 'liked'})
	else:
	    return Response({'status': 'already voted'})

    @detail_route(methods=['post'], url_path='dislike')
    def dislike(self, request, pk=None):
        if not pk in request.session.get('dislikes', []):
            candidato = get_object_or_404(Candidato, pk)
            candidato.dislike()
            if request.session.get('dislikes', False):
                request.session['dislikes'].append(pk)
            else:
                request.session['dislikes'] = [pk]
