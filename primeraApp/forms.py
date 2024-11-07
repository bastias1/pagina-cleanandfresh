from django import forms
from django.core import validators
from primeraApp.models import *

class RegistroEmpleados(forms.ModelForm):
    class Meta:
        model = Empleado 
        fields = ('nombre', 'apellido', 'rut', 'correo', 'telefono', 'password') 

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'apellido' : forms.TextInput(attrs={'class':'form-control'}),
            'rut' : forms.TextInput(attrs={'class':'form-control'}),
            'correo' : forms.EmailInput(attrs={'class':'form-control'}),
            'telefono' : forms.NumberInput(attrs={'class':'form-control'}),
            'password' : forms.TextInput(attrs={'class':'form-control'}),
        }

class IngresoServicios(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombreServicio','duracion','descripcion']

class IngresoCita(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['fecha','estado','cliente','vehiculo','servicio']


