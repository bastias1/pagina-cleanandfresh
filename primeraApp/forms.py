from django import forms
from django.core import validators
from primeraApp.models import *

class RegistroEmpleados(forms.ModelForm):
    
    class Meta:
        model = Empleado
        fields = ['nombre','email','contraseña','telefono']

class IngresoServicios(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombreServicio','duracion','descripcion']

class IngresoCita(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['fecha','estado','cliente','vehiculo','servicio']


