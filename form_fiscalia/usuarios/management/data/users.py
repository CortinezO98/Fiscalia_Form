import os
from usuarios.enums import *

ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', '1234')
STAFF_PASSWORD = os.environ.get('STAFF_PASSWORD', '1234')

users = [
    {
        "username": "admin", 
        "password": ADMIN_PASSWORD,
        "is_superuser": True,
        "is_staff": True,
        "role_id": Roles.ADMINISTRADOR.value
    },
    {
        "username": "jcortinezo", 
        "password": ADMIN_PASSWORD,
        "is_superuser": True,
        "is_staff": True,
        "role_id": Roles.ADMINISTRADOR.value
    },
    {
        "username": "supervisor", 
        "password": STAFF_PASSWORD,
        "is_superuser": False,
        "is_staff": False,
        "role_id": Roles.SUPERVISOR.value
    },
    {
        "username": "agente", 
        "password": STAFF_PASSWORD,
        "is_superuser": False,
        "is_staff": False,
        "role_id": Roles.AGENTE.value
    },
]