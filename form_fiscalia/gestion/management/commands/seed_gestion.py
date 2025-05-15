from django.core.management.base import BaseCommand
from django.db import transaction
from gestion.models import *
from gestion.management.data.segmentos import segmentos

class Command(BaseCommand):
    help = 'Carga datos de prueba en la base de datos gestion'

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                CrearSegmentos()
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