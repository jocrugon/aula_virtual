from django.urls import path
from apps.aula_virtual.views import *

urlpatterns = [
    path('inicio/',Bienvenida,name='inicio'),
    path('perfil/',Perfil,name='perfil'),
    path('cursos/',Cursos,name='cursos'),
]