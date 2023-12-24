from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    CHOICE = (
        ('Training', 'Training'),
        ('Personal coach', 'Personal coach')
    )
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    imagen = models.ImageField(upload_to='imagenes_usuarios')
    rol = models.CharField(max_length=20, choices=CHOICE, null=True, blank=True)
    
    def __str__(self):
        return "Usuario: " + self.usuario.username + ", Rol del usuario: " + str(self.rol)