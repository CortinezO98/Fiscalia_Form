from django.core.management.base import BaseCommand
from django.db import transaction
from gestion.models import *
from gestion.management.data.segmentos import segmentos
from gestion.management.data.tipificaciones import tipificaciones
from gestion.management.data.categorias import categorias

class Command(BaseCommand):
    help = 'Carga datos de prueba en la base de datos gestion'

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                CrearSegmentos()
                CrearTipificaciones()
                CrearCategorias()
                self.stdout.write(self.style.SUCCESS('Datos de prueba cargados correctamente.'))
        except Exception as e:
            self.stdout.write(self.style.SUCCESS('Error, se hizo rollback'+e))


def CrearSegmentos():
    for segmentoData in segmentos:
        segmento = Segmento.objects.filter(id=segmentoData['id']).first()
        if not segmento:
            Segmento.objects.create(
                id=segmentoData['id'],
                nombre=segmentoData['nombre']
            )

def CrearTipificaciones():
    for tipificacionData in tipificaciones:
        tipificacion = Tipificacion.objects.filter(id=tipificacionData['id']).first()
        if not tipificacion:
            Tipificacion.objects.create(
                id=tipificacionData['id'],
                nombre=tipificacionData['nombre'],
                segmento_id=int(tipificacionData['segmento_id'])
            )

def CrearCategorias():
    for categoriaData in categorias:
        categoria = Categoria.objects.filter(id=categoriaData['id']).first()
        if not categoria:
            categoria = Categoria(
                id=categoriaData['id'],
                nombre=categoriaData['nombre'],
                nivel=int(categoriaData['nivel'])  
            )
            if categoriaData['tipificacion_id']:
                categoria.tipificacion_id=int(categoriaData['tipificacion_id'])

            if categoriaData['categoria_padre_id']:
                categoria.categoria_padre_id=int(categoriaData['categoria_padre_id'])
            
            categoria.save()