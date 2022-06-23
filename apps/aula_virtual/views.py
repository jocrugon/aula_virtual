import re
from django.shortcuts import render

# Create your views here.

def Bienvenida(request):
    return render(request, 'aula_virtual/bienvenida.html')

def Perfil(request):
    return render(request,'aula_virtual/perfil.html')

def Cursos(request):
    return render(request,'aula_virtual/cursos.html')