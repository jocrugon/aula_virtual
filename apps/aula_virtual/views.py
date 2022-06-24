from django.shortcuts import render
from django.views.generic import View, TemplateView, UpdateView, ListView

from apps.aula_virtual.forms import PersonaForm
from .models import *
# Create your views here.


class Bienvenida(TemplateView):
    template_name = "aula_virtual/bienvenida.html"
    

''' class Persona(ListView):
    
    model = Persona
    template_name = "aula_virtual/perfil.html"
    context_object_name = 'personas'
    
    def get_queryset(self):
        qs = super(Persona, self).get_queryset()
        return qs.filter(id=self.kwargs.get('id')).first() '''

class Docente(ListView):
    
    model = Docente
    template_name = "aula_virtual/perfil.html"
    context_object_name = 'docentes'
    
    def get_queryset(self):
        qs = super(Docente, self).get_queryset()
        return qs.filter(id=self.kwargs.get('id')).first()
    

def Cursos(request):
    return render(request,'aula_virtual/cursos.html')

