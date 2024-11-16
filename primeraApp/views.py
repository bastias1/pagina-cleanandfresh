from django.shortcuts import render,redirect
from . import forms
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import RegistroEmpleados
# Create your views here.

#Paginas que ve el Cliente
def index(request):
    return render(request,'user/index.html')

def servicios(request):
    servicios = Servicio.objects.all()  # Obtén todos los servicios desde la base de datos
    return render(request, 'user/servicios.html', {'servicios': servicios})


def agendar(request):
    form_cita = forms.CitaForm()

    if request.method=='POST':
        form_cita = forms.CitaForm(request.POST)
        print("Form Insertado")
        if form_cita.is_valid():
            print("Datos insertados a la base de datos")
            print(form_cita.cleaned_data)
            form_cita.save()
    else:
        print("Datos NO insertados")
        form_cita = forms.CitaForm()
    
    return render(request,'user/agendar.html',{'form_cita':form_cita})

#Paginas que ven los Empleados/Admin
def login(request):
    return render(request, 'admin/login.html')

@login_required
def adminDashboard(request):
    return render(request, 'admin/dashboard.html')

@login_required
def dashboardHorasAgendadas(request):
    return render(request, 'admin/horasAgendadasDashboard.html')

#GESTION EMPLEADO 
def gestionarEmpleados(request):
    empleados = Empleado.objects.all()
    
    data = {
        'empleados':empleados
    }
    return render(request, 'admin/gestionarUsuarios.html',data)

def eliminarEmpleado(request,id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    print("empleado eliminado")
    return redirect('/gestion-empleados')
    
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

##
def modificarEmpleado(request, id):
    empleado = Empleado.objects.get(id=id)
    form = RegistroEmpleados(instance=empleado)
    
    if request.method == "POST":
        form = RegistroEmpleados(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            print("Empleado modificado correctamente")
            return redirect('crearUsuario')  # Redirige a la vista de creación de empleados (registro_empleados_view)
    
    data = {'form': form}
    return render(request, 'admin/crearUsuarios.html', data)


def eliminarServicio(request, id):
    servicio = Servicio.objects.get(id=id)
    servicio.delete()
    print("Servicio eliminado")
    return redirect('gestionServicios')

def gestionServicios(request):
    servicios=Servicio.objects.all()
    return render(request, 'admin/serviciosDashboard.html',{'servicios':servicios})

def agregarServicio(request):
    if request.method == 'POST':
        form = forms.IngresoServicios(request.POST, request.FILES)
        if form.is_valid():
            print("Datos insertados a la base de datos")
            form.save()
            return redirect('gestionServicios')  
        else:
            print("Datos NO insertados")
    else:
        form = forms.IngresoServicios()  

    return render(request, 'admin/agregarServicios.html', {'form': form})


def modificarServicio(request, id):
    servicio = Servicio.objects.get(id=id)  

    if request.method == 'POST':
        form = forms.IngresoServicios(request.POST, request.FILES, instance=servicio)
        if form.is_valid():
            form.save()
            print("Servicio modificado correctamente")
            return redirect('gestionServicios')
    else:
        form = forms.IngresoServicios(instance=servicio)

    # Reutiliza la plantilla de agregar servicios
    return render(request, 'admin/agregarServicios.html', {'form': form, 'es_modificar': True, 'servicio': servicio})
