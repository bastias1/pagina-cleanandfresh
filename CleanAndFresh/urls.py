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

urlpatterns = [
    path('admin/', admin.site.urls),
    #Inicio vista Cliente
    path('',views.index,name='index'),
    path('servicios/',views.servicios),
    path('login/',views.login),
    path('agendar/',views.agendar),
    #Fin vista cliente

    #Inicio vista Empleados/Admin
    path('adminDashboard/', views.adminDashboard),
    path('gestion-horas-agendadas/',views.dashboardHorasAgendadas),
    path('creacion-empleados/',views.registro_empleados_view, name='crearUsuario'),
    path ('gestion-empleados/', views.gestionarEmpleados),
    path('eliminar-empleado/<int:id>',views.eliminarEmpleado),
    path('modificar-empleado/<int:id>',views.modificarEmpleado, name='modificarEmpleado'),
    path('gestion-servicios/',views.gestionServicios,name='gestionServicios'),
    path('agregar-servicios/',views.agregarServicio),
    path('eliminar-servicio/<int:id>/', views.eliminarServicio, name='eliminarServicio'),
    path('modificar-servicio/<int:id>/', views.modificarServicio, name='modificarServicio'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#lo que esta despues del ']' hace la magia con las imagenes