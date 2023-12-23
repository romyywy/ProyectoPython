from django.db import models

# Create your models here.

class alumno(models.Model):
    nombre = models.CharField(max_length=60)
    objetivo = models.CharField(max_length=100)
    ultima_rutina=models.CharField(max_length=30,)
    def __str__(self):
        return self.nombre 

