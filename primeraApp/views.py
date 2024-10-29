from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'index.html')

def servicios(request):
    return render(request,'servicios.html')

def agendar(request):
    return render(request,'agendar.html')

def login(request):
    return render(request,'login.html')

def dashboardHorasAgendadas(request):
    return render(request,'horasAgendadasDashboard.html')

def dashboardCreacionUsuarios(request):
    form=forms.RegistroEmpleados()
    if request.method=='POST':
        form=forms.RegistroEmpleados(request.POST)
        if form.is_valid():
            print("Formulario OK")
            print("nombre",form.cleaned_data['nombre'])
            print("apellido", form.cleaned_data['apellido'])
            print("email",form.cleaned_data['email'])
            print("fono",form.cleaned_data['fono'])
    data = {'form' : form}
    return render(request, 'creacionUsuariosDashboard.html', data)


def dashboardEliminarUsuarios(request):
    return render(request, 'eliminarUsuariosDashboard.html')

def test(request):
    return render(request,'test.html')