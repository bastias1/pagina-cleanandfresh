from django.db import models

class Empleado(models.Model):
    rut = models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo= models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    telefono = models.BigIntegerField()

    def __srt__(self):
        return self.nombre

class Servicio(models.Model):
    nombreServicio = models.CharField(max_length=100)
    duracion = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField()

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
    estado = models.CharField(max_length=50)
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)
    servicio = models.ManyToManyField(Servicio)