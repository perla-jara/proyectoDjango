from django.db import models
from django.utils import timezone

# Create your models here.
class Pedido(models.Model):
    n_boleta = models.IntegerField()
    nombre = models.CharField(max_length=30)
    fecha = models.DateTimeField(auto_now=True)
    hora = models.DateTimeField(default=timezone.now)
    detalle = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    rut = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    celular = models.CharField(max_length=12)
    contraseña = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


