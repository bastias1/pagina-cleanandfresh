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
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    #Inicio vista Cliente
    path('',views.index),
    path('servicios/',views.servicios),
    path('agendar/',views.agendar),
    #Fin vista cliente

    #Inicio vista Empleados/Admin
<<<<<<< HEAD
    path('adminDashboard/', views.adminDashboard),
    path('gestion-horas-agendadas/',views.dashboardHorasAgendadas),
    path('creacion-empleados/',views.registro_empleados_view),
    path ('gestion-empleados/', views.gestionarEmpleados),
    path('eliminar-empleado/<int:id>',views.eliminarEmpleado),
    path('modificar-empleado/<int:id>',views.eliminarEmpleado),
    path('gestion-servicios/',views.gestionServicios,name='gestionServicios'),
    path('agregar-servicios/',views.agregarServicio),
    path('eliminar-servicio/<int:id>/', views.eliminarServicio, name='eliminarServicio'),

=======
     path('login/',auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('adminDashboard/', login_required(views.adminDashboard)),
    path('gestion-horas-agendadas/',login_required(views.dashboardHorasAgendadas)),
    path('creacion-empleados/',login_required(views.registro_empleados_view)),
    path ('gestion-empleados/', login_required(views.gestionarEmpleados)),
    path('eliminar-empleado/<int:id>',login_required(views.eliminarEmpleado)),
    path('modificar-empleado/<int:id>',login_required(views.eliminarEmpleado)),
    path('gestion-servicios/',login_required(views.gestionServicios),name='gestionServicios'),
    path('agregar-servicios/',login_required(views.agregarServicio)),
>>>>>>> 7b1dec9eb56857a1c46c010dc8328fcb7f7d1448

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#lo que esta despues del ']' hace la magia con las imagenes