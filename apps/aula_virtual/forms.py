from dataclasses import field
from django import forms
from .models import *

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        
        
