from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User
from django.db import transaction
from usuarios.management.data.users import users
from usuarios.models import *
from usuarios.enums import *

class Command(BaseCommand):
    help = 'Carga datos de prueba en la base de datos'

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                CreateRoles()
                CreateUsers()
                self.stdout.write(self.style.SUCCESS('Datos creados correctamente.'))
        except Exception as e:
            self.stdout.write(self.style.SUCCESS('Error, se hizo rollback'+e))

def CreateRoles():
    Group.objects.create(id=Roles.ADMINISTRADOR.value, name=Roles.ADMINISTRADOR.label)
    Group.objects.create(id=Roles.SUPERVISOR.value, name=Roles.SUPERVISOR.label)
    Group.objects.create(id=Roles.AGENTE.value, name=Roles.AGENTE.label)

def CreateUsers():
    for userData in users:
        user = User.objects.filter(username=userData['username']).first()
        if not user:
            user = User.objects.create_user(
                username = userData['username'],
                password = userData['password'],
                is_staff = userData['is_staff'],
                is_superuser = userData['is_superuser']
            )
            group = Group.objects.filter(id=userData['role_id']).first()
            if group:
                user.groups.add(group)
                print(user, group)