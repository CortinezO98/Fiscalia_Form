from django.core.management.base import BaseCommand
from django.db import transaction
from gestion.models import *
from gestion.management.data.tiposIdentificacion import tiposIdentificacion
from gestion.management.data.segmentos import segmentos
from gestion.management.data.tipificaciones import tipificaciones
from gestion.management.data.categorias import categorias

class Command(BaseCommand):
    help = 'Carga datos de prueba en la base de datos gestion'

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                CrearTiposIdentificacion()
                CrearSegmentos()
                CrearTipificaciones()
                CrearCategorias()
                self.stdout.write(self.style.SUCCESS('Datos de creados correctamente.'))
        except Exception as e:
            self.stdout.write(self.style.SUCCESS('Error, se hizo rollback'+e))

def CrearTiposIdentificacion():
    for tipoIdentificacionData in tiposIdentificacion:
        tipoIdentificacion = TipoIdentificacion.objects.filter(id=tipoIdentificacionData['id']).first()
        if not tipoIdentificacion:
            TipoIdentificacion.objects.create(
                id=tipoIdentificacionData['id'],
                nombre=tipoIdentificacionData['nombre']
            )
    print('CrearTiposIdentificacion se ejecutó correctamente.')


def CrearSegmentos():
    for segmentoData in segmentos:
        segmento = Segmento.objects.filter(id=segmentoData['id']).first()
        if not segmento:
            Segmento.objects.create(
                id=segmentoData['id'],
                nombre=segmentoData['nombre']
            )
    print('CrearSegmentos se ejecutó correctamente.')

def CrearTipificaciones():
    for tipificacionData in tipificaciones:
        tipificacion = Tipificacion.objects.filter(id=tipificacionData['id']).first()
        if not tipificacion:
            Tipificacion.objects.create(
                id=tipificacionData['id'],
                nombre=tipificacionData['nombre'],
                segmento_id=int(tipificacionData['segmento_id'])
            )
    print('CrearTipificaciones se ejecutó correctamente.')

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
    print('CrearCategorias se ejecutó correctamente.')