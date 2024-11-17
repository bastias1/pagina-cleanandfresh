from django.db import models

class Empleado(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    telefono = models.BigIntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Servicio(models.Model):
    nombreServicio = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='servicios/', null=True, blank=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombreServicio

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    correo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Vehiculo(models.Model):
    patente = models.CharField(max_length=50)
    año = models.IntegerField()
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    dueño = models.ForeignKey(Cliente,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.patente})"

class Cita(models.Model):
    fecha = models.DateField()
    vehiculo = models.ForeignKey(Vehiculo, null=True, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)
    servicio = models.ManyToManyField(Servicio)

    def __str__(self):
        cliente_nombre = self.cliente.nombre if self.cliente else "Sin Cliente"
        return f"Cita para {cliente_nombre} el {self.fecha}"
