"""
URL configuration for cleanandfresh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from primeraApp import views
#estas 2 lineas de abajo son las librerias para agregar imagenes
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    #Inicio vista Cliente
    path('',views.index,name='index'),
    path('servicios/',views.servicios),
    path('agendar/',views.agendar),
    #Fin vista cliente

    #Inicio vista Empleados/Admin
    path('login/',views.inicioSesion,name='login'),
    path('logout/',views.cerrarSesion,name='logout'),
    path('adminDashboard/',login_required(views.adminDashboard),name='adminDashboard'),
    #Gestion Citas
    path('gestion-citas/',login_required(views.dashboardHorasAgendadas),name='gestion-citas'),
    path('agendar-cita/',login_required(views.agendarCitaEmpleado)),
    path('modificar-cita/<int:id>/',login_required(views.modificarCita),name='modificarCita'),
    path('eliminar-cita/<int:id>/',login_required(views.eliminarCita),name='eliminarCita'),

    #Gestion Empleados
    path('creacion-empleados/',login_required(views.registro_empleados_view)),
    path ('gestion-empleados/', login_required(views.gestionarEmpleados),name='gestionEmpleado'),
    path('eliminar-empleado/<int:id>',login_required(views.eliminarEmpleado)),
    path('modificar-empleado/<int:id>',login_required(views.modificarEmpleado), name='modificarEmpleado'),

    #Gestion Servicios
    path('gestion-servicios/',login_required(views.gestionServicios),name='gestionServicios'),
    path('agregar-servicios/',login_required(views.agregarServicio)),
    path('eliminar-servicio/<int:id>/', login_required(views.eliminarServicio), name='eliminarServicio'),
    path('modificar-servicio/<int:id>/', login_required(views.modificarServicio), name='modificarServicio'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#lo que esta despues del ']' hace la magia con las imagenes