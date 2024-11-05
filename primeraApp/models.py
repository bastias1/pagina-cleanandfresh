from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre=models.CharField(max_length=50)
    email= models.EmailField(max_length=50)
    contraseña = models.CharField(max_length=100)

class Servicio(models.Model):
    nombreServicio = models.CharField(max_length=100)
    duracion = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()

class Vehiculo(models.Model):
    patente =models.CharField(max_length=50)
    año = models.IntegerField()
    marca =models.CharField(max_length=50)
    modelo =models.CharField(max_length=50)

class Cliente(models.Model):
    nombre =models.CharField(max_length=50)
    telefono =models.CharField(max_length=50)
    correo =models.CharField(max_length=50)

class Cita(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    tipoServicio = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cliente = models.OneToOneField(Cliente)
    vehiculo = models.OneToOneField(Vehiculo)