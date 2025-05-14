from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group

def en_grupo(grupo_nombre):
    def decorator(func):
        def wrap(request, *args, **kwargs):
            if not request.user.groups.filter(name=grupo_nombre).exists():
                return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
            return func(request, *args, **kwargs)
        return wrap
    return decorator