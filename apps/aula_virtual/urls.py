from django.urls import path
from apps.aula_virtual.views import *

urlpatterns = [
    path('inicio/',Bienvenida.as_view(),name='inicio'),
    path('perfil/<int:id>',Persona.as_view(),name='perfil'),
    path('cursos/<int:id>',Cursos.as_view(),name='cursos'),
    
]
