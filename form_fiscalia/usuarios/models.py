from django.db import models
from django.contrib.auth.models import User



class Tipificacion(models.Model):
    cedula = models.CharField(max_length=20)
    agente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuarios_tipificacion_set')  # Añadí el related_name aquí
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cedula} - {self.fecha}"