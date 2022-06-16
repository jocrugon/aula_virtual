from django.urls import path
from apps.aula_virtual.views import *

urlpatterns = [
    path('bienvenida/',Bienvenida,name='bienvenida'),
]