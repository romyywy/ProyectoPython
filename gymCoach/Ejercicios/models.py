from django.db import models

# Create your models here.


class Ejercicio(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=100)
    grupo_muscular=models.CharField(max_length=30, default='general')
    def __str__(self):
        return self.nombre 

