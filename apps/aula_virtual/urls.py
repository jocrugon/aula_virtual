from django.urls import path
from apps.aula_virtual.views import *

urlpatterns = [
    path('inicio/',Bienvenida.as_view(),name='inicio'),
    path('perfil/<int:id>',Docente.as_view(),name='perfil'),
    path('cursos/',Cursos,name='cursos'),
    
]