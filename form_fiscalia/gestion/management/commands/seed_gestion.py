from django.core.management.base import BaseCommand
from gestion.models import *

class Command(BaseCommand):
    help = 'Carga datos de prueba en la base de datos gestion'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Datos de prueba cargados correctamente. gestion'))
