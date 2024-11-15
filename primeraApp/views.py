from django.shortcuts import render
from . import forms
from .models import *
# Create your views here.

#Paginas que ve el Cliente
def index(request):
    return render(request,'user/index.html')

def servicios(request):
    return render(request,'user/servicios.html')

def agendar(request):
    if request.method=='POST':
        cliente_form = forms.ClienteForm(request.POST)
        vehiculo_form = forms.VehiculoForm(request.POST)
        cita_form = forms.CitaForm(request.POST)
        print(request.POST)

        if cliente_form.is_valid() and vehiculo_form.is_valid():
            print("Cliente valid")
            print("Vehiculo Valid")
            cliente = cliente_form.save()
            vehiculo = vehiculo_form.save()

            cita = cita_form.save(commit=False)
            cita.cliente = cliente
            cita.vehiculo = vehiculo
            cita.save()
            cita_form.save_m2m()
            print("Cita Guardada Correctamente")
    else:
        cliente_form = forms.ClienteForm()
        vehiculo_form = forms.VehiculoForm()
        cita_form = forms.CitaForm()

    return render(request,'user/agendar.html',{'cliente_form':cliente_form,'vehiculo_form':vehiculo_form,'cita_form':cita_form})

#Paginas que ven los Empleados/Admin
def login(request):
    return render(request,'admin/login.html')

def adminDashboard(request):
    return render(request,'admin/dashboard.html')

def dashboardHorasAgendadas(request):
    return render(request,'admin/horasAgendadasDashboard.html')

def gestionarEmpleados(request):
    empleados = Empleado.objects.all()
    selected_empleado = None

    if request.method == 'POST':
        form = forms.

    return render(request, 'admin/gestionarUsuarios.html')

def registro_empleados_view(request):
    form = forms.RegistroEmpleados()
    if request.method=='POST':
        form = forms.RegistroEmpleados(request.POST)
        print("Form Insertado")
        if form.is_valid():
            print("Datos insertados a la base de datos")
            form.save()
    else:
        print("Datos NO insertados")
        form = forms.RegistroEmpleados()
    
    return render(request,'admin/crearUsuarios.html',{'form':form})



def gestionServicios(request):
    return render(request, 'admin/serviciosDashboard.html')

#def modificarServicio(request):    

    