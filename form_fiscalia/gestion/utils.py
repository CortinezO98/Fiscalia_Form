from .models import *

def RegistrarError(metodo, excepcion, request):
    try:
        RegistroError.objects.create(
            metodo=metodo,
            excepcion=excepcion,
            usuario= request.user if request.user.is_authenticated else None,
        )
    except Exception as e:
        print(f"Error al registrar la excepción: {e}")