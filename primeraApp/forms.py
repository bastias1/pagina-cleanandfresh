from django import forms
from django.core import validators
from primeraApp.models import *
import datetime
from django import forms
from .models import Cita

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
        fields = ['fecha', 'servicio']  # Excluir 'cliente' y 'vehiculo'
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'servicio': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }
    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']

        # Validar que la fecha no sea un sábado o domingo
        if fecha.weekday() in [5, 6]:  # 5 = sábado, 6 = domingo
            raise forms.ValidationError("No se pueden agendar citas en fines de semana. Por favor selecciona un día hábil.")

        # Validar que la fecha no sea anterior a la fecha actual
        if fecha < datetime.date.today():
            raise forms.ValidationError("No se pueden agendar citas en fechas pasadas. Por favor selecciona una fecha futura.")

        return fecha

class IngresoServicios(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombreServicio','descripcion','imagen']
        widget = {
            'nombreServicio': forms.TextInput(attrs={'class' : 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'imagen':forms.ClearableFileInput(attrs={'class':'form-control'}),
        }