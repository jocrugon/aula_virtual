from django.shortcuts import render
from django.views.generic import View, TemplateView, UpdateView, ListView

from apps.aula_virtual.forms import PersonaForm
from .models import *
# Create your views here.


class Bienvenida(TemplateView):
    template_name = "aula_virtual/bienvenida.html"
    

class Persona(ListView):
    model = Persona
    template_name = "aula_virtual/perfil.html"
    context_object_name = 'personas'
    
    def get_queryset(self):
        qs = super(Persona, self).get_queryset()
        return qs.filter(usuario=self.kwargs.get('id')).first()

class Cursos(ListView):
    model = Detalle_alumno_en_curso
    template_name = "aula_virtual/cursos.html"
    context_object_name = 'alumno_en_curso'
    
    def get_queryset(self):
        return Detalle_alumno_en_curso.objects.filter(usuario=self.request.resolver_match.kwargs['id'])

