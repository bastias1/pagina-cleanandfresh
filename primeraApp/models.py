from django.db import models

class Empleado(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    telefono = models.BigIntegerField()

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombreServicio = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombreServicio

class Vehiculo(models.Model):
    patente = models.CharField(max_length=50)
    año = models.IntegerField()
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.patente})"

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    correo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    fecha = models.DateField()
    estado = models.CharField(max_length=50)
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)  # Usar ForeignKey para una relacion 1 a muchos
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)  # Usar ForeignKey para una relacion 1 a muchos
    servicio = models.ManyToManyField(Servicio)

    def __str__(self):
        return f"Cita on {self.fecha} - {self.cliente.nombre}"
