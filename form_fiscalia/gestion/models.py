from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TipoIdentificacion(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tipo documento"
        verbose_name_plural = "Tipos de documentos"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre}"

class Ciudadano(models.Model):
    tipo_identificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.CASCADE)
    numero_identificacion = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Ciudadano"
        verbose_name_plural = "Ciudadanos"
        indexes = [models.Index(fields=['numero_identificacion'])]

    def __str__(self):
        return f"{self.nombre} ({self.tipo_identificacion} {self.numero_identificacion})"

class Segmento(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Segmento"
        verbose_name_plural = "Segmentos"
        ordering = ['id']

    def __str__(self):
        return self.nombre

class Tipificacion(models.Model):
    nombre = models.CharField(max_length=200)
    segmento = models.ForeignKey(Segmento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Tipificación"
        verbose_name_plural = "Tipificaciones"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    nivel = models.IntegerField(default=1, db_index=True)
    tipificacion = models.ForeignKey(Tipificacion, null=True, blank=True, on_delete=models.CASCADE)
    categoria_padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='categoriapadre')

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nombre']

    def __str__(self):
        if self.tipificacion:
            return f"{self.nombre} [{self.nivel}] - {self.tipificacion} - {self.tipificacion.segmento.nombre}"
        else:
            return f"{self.nombre} [{self.nivel}] - {self.categoria_padre.nombre}"


class Evaluacion(models.Model):
    conversacion_id = models.CharField(max_length=250)
    observacion = models.TextField()
    ciudadano = models.ForeignKey(Ciudadano, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now=True)


class RegistroError(models.Model):
    metodo = models.CharField(max_length=100)
    excepcion = models.TextField()
    fecha = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)