from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    rut = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    celular = models.CharField(max_length=12)
    contraseña = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


