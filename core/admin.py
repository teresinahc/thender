from django.contrib import admin
from .models import Candidato, Legenda, Posicionamento

# Register your models here.
admin.site.register(Candidato)
admin.site.register(Legenda)
admin.site.register(Posicionamento)
