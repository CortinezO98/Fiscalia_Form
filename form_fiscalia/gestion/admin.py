from django.contrib import admin
from .models import *

@admin.register(TipoIdentificacion)
class TipoIdentificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Ciudadano)
class CiudadanoAdmin(admin.ModelAdmin):
    list_display = ('nombre','tipo_identificacion','numero_identificacion','correo','telefono','pais','ciudad',)
    search_fields = ('nombre','numero_identificacion','correo','telefono',)
    list_filter = ('tipo_identificacion','pais',)


@admin.register(Segmento)
class SegmentoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('id',)


@admin.register(Tipificacion)
class TipificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'segmento')
    list_filter = ('segmento',)
    search_fields = ('nombre',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel', 'tipificacion', 'categoria_padre')
    list_filter = ('nivel', 'tipificacion')
    search_fields = ('nombre',)


@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ('ciudadano', 'categoria', 'user', 'fecha')
    list_filter = ('fecha', 'user', 'categoria')
    search_fields = ('ciudadano__nombre', 'observacion')