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
        fields = ['nombreServicio','descripcion']
        widgets = {
            'nombreServicio' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
        }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','apellido','telefono','correo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.EmailInput(attrs={'class':'form-control'}),
        }

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente','año','marca','modelo']
        widgets = {
            'patente': forms.TextInput(attrs={'class':'form-control'}),
            'año': forms.NumberInput(attrs={'class':'form-control'}),
            'marca': forms.TextInput(attrs={'class':'form-control'}),
            'modelo': forms.TextInput(attrs={'class':'form-control'}),
        }

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [ 'cliente', 'vehiculo','fecha', 'servicio'] 
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'servicio': forms.SelectMultiple(),
        }

class IngresoServicios(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombreServicio','descripcion','imagen']
        widget = {
            'nombreServicio': forms.TextInput(attrs={'class' : 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'imagen':forms.ClearableFileInput(attrs={'class':'form-control'}),
        }