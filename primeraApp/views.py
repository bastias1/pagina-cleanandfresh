from django.shortcuts import render,redirect
from . import forms
from .models import *
from .forms import RegistroEmpleados
# Create your views here.

#Paginas que ve el Cliente
def index(request):
    return render(request,'user/index.html')

def servicios(request):
    servicios = Servicio.objects.all()  # Obtén todos los servicios desde la base de datos
    return render(request, 'user/servicios.html', {'servicios': servicios})


def agendar(request):
    if request.method == 'POST':
        cliente_form = forms.ClienteForm(request.POST)
        vehiculo_form = forms.VehiculoForm(request.POST)
        cita_form = forms.CitaForm(request.POST)

        if cliente_form.is_valid() and vehiculo_form.is_valid() and cita_form.is_valid():
            cliente = cliente_form.save()
            vehiculo = vehiculo_form.save()
            cita = cita_form.save(commit=False)
            cita.cliente = cliente
            cita.vehiculo = vehiculo
            cita.save()
            cita_form.save_m2m()
            print("Cita guardada correctamente")
            return redirect('index')  # Redirigir a la URL raíz
        else:
            print("Errores en los formularios")
    else:
        cliente_form = forms.ClienteForm()
        vehiculo_form = forms.VehiculoForm()
        cita_form = forms.CitaForm()

    return render(request, 'user/agendar.html', {
        'cliente_form': cliente_form,
        'vehiculo_form': vehiculo_form,
        'cita_form': cita_form,
    })



#hacer que el agendar utilice los datos del cliente con los del vehiculo en los datos de la cita#


#Paginas que ven los Empleados/Admin
def login(request):
    return render(request, 'admin/login.html')

def adminDashboard(request):
    return render(request, 'admin/dashboard.html')


#Gestion Cita
def dashboardHorasAgendadas(request):
    citas = Cita.objects.all()
    servicios = Servicio.objects.all()

    data = {
        'citas':citas,
        'servicios':servicios
    }
    return render(request, 'admin/horasAgendadasDashboard.html',data)

def agendarCitaEmpleado(request):
    if request.method == 'POST':
        cliente_form = forms.ClienteForm(request.POST)
        vehiculo_form = forms.VehiculoForm(request.POST)
        cita_form = forms.CitaForm(request.POST)

        if cliente_form.is_valid() and vehiculo_form.is_valid() and cita_form.is_valid():
            cliente = cliente_form.save()
            vehiculo = vehiculo_form.save(commit=False)
            vehiculo.dueño = cliente
            vehiculo.save()
            cita = cita_form.save(commit=False)
            cita.cliente = cliente
            cita.vehiculo = vehiculo
            cita.save()
            cita_form.save_m2m()
            print("Cita guardada correctamente")
            return redirect('gestion-citas')  # Redirigir a la URL raíz
        else:
            print("Errores en los formularios")
    else:
        cliente_form = forms.ClienteForm()
        vehiculo_form = forms.VehiculoForm()
        cita_form = forms.CitaForm()

    return render(request, 'admin/agendarEmpleados.html', {
        'cliente_form': cliente_form,
        'vehiculo_form': vehiculo_form,
        'cita_form': cita_form,
    })

def modificarCita(request,id):
    pass

def eliminarCita(request, id):
    try:
        cita = Cita.objects.get(id=id)
        cita.servicio.clear() 
        cita.vehiculo.delete()
        cita.cliente.delete()
        cita.delete()
        print("Cita eliminada")
    except Exception as e:
        print(f"Error deleting cita: {e}")
    
    return redirect('gestion-citas')


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
