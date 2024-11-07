from django.shortcuts import render
from . import forms
# Create your views here.

#Paginas que ve el Cliente
def index(request):
    return render(request,'user/index.html')

def servicios(request):
    return render(request,'user/servicios.html')

def agendar(request):
    return render(request,'user/agendar.html')

#Paginas que ven los Empleados/Admin
def login(request):
    return render(request,'admin/login.html')

def adminDashboard(request):
    return render(request,'admin/dashboard.html')

def dashboardHorasAgendadas(request):
    return render(request,'admin/horasAgendadasDashboard.html')

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
    
    return render(request,'admin/creacionUsuariosDashboard.html',{'form':form})

def dashboardEliminarUsuarios(request):
    return render(request, 'admin/eliminarUsuariosDashboard.html')