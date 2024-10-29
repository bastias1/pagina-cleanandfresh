from django import forms
from django.core import validators

class RegistroEmpleados(forms.Form):

    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(4),
        validators.MaxLengthValidator(20)
    ])
    apellido = forms.CharField(validators=[
        validators.MinLengthValidator(4),
        validators.MaxLengthValidator(20)
        ])
    email =  forms.CharField(widget=forms.EmailInput) 
    fono =  forms.CharField(required=False)


    nombre.widget.attrs['class'] = 'form-control'


