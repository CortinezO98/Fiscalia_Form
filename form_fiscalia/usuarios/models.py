from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Ciudadano(models.Model):
    TIPO_ID_CHOICES = [
        ('CC', 'Cédula de ciudadanía'),
        ('TI', 'Tarjeta de identidad'),
        ('CE', 'Cédula de extranjería'),
    ]
    
    tipo_identificacion = models.CharField(max_length=2, choices=TIPO_ID_CHOICES)
    numero_identificacion = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ciudadano"
        verbose_name_plural = "Ciudadanos"
        indexes = [models.Index(fields=['numero_identificacion'])]
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.nombre} ({self.tipo_identificacion} {self.numero_identificacion})"
    
    


class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='supervisor')
    nombre = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Supervisor"
        verbose_name_plural = "Supervisores"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre

class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='administrador')
    nombre = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre


class Agente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='agente')
    nombre = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Agente"
        verbose_name_plural = "Agentes"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre

class Formulario(models.Model):
    nombre = models.CharField(max_length=255, help_text="Nombre del formulario principal")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Formulario"
        verbose_name_plural = "Formularios"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Opcion(models.Model):
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE, related_name='opciones')
    texto = models.CharField(max_length=255)
    opcion_padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subopciones')
    orden = models.PositiveIntegerField(default=0)
    requiere_observacion = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Opción"
        verbose_name_plural = "Opciones"
        ordering = ['orden']

    def __str__(self):
        return f"{self.formulario.nombre} - {self.texto}"

class Evaluacion(models.Model):
    ESTADOS = (
        ('B', 'Borrador'),
        ('C', 'Completada'),
        ('A', 'Archivada'),
    )
    
    consecutivo = models.CharField(max_length=100, unique=True)
    ciudadano = models.ForeignKey(Ciudadano, on_delete=models.PROTECT, related_name='evaluaciones')
    agente = models.ForeignKey(Agente, on_delete=models.PROTECT, related_name='evaluaciones')
    formulario = models.ForeignKey(Formulario, on_delete=models.PROTECT, null=True, blank=True)
    fecha_inicio = models.DateTimeField(default=timezone.now)
    id_conversacion = models.CharField(max_length=100, unique=True)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='B')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Evaluación"
        verbose_name_plural = "Evaluaciones"
        indexes = [
            models.Index(fields=['consecutivo']),
            models.Index(fields=['id_conversacion']),
        ]
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"Evaluación {self.consecutivo} - {self.ciudadano.nombre}"

class Tipificacion(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE, related_name='tipificaciones', null=True, blank=True)
    opcion = models.ForeignKey(Opcion, on_delete=models.PROTECT, null=True, blank=True)
    valor = models.TextField()
    observaciones = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Tipificación"
        verbose_name_plural = "Tipificaciones"
        unique_together = ('evaluacion', 'opcion')
        ordering = ['opcion__orden']

    def __str__(self):
        return f"{self.opcion.texto} - {self.valor[:50]}"