from django.shortcuts import render

# Create your views here.
def Bienvenida(request):
    return render(request, 'aula_virtual/bienvenida.html')
