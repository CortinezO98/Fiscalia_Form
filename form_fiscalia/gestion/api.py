from django.http import JsonResponse
from .models import *

def ciudadano(request):
    numero_identificacion = request.GET.get('numero_identificacion')
    if numero_identificacion:
        try:
            ciudadano = Ciudadano.objects.get(numero_identificacion=numero_identificacion)
            return JsonResponse({
                'id': ciudadano.id,
                'nombre': ciudadano.nombre,
                'tipo_identificacion_id': ciudadano.tipo_identificacion.id,
            })
        except Ciudadano.DoesNotExist:
            return JsonResponse({}, status=404)
    return JsonResponse({'error': 'Número no enviado'}, status=400)

def tipificaciones(request):
    segmento_id = request.GET.get('segmento_id')
    if segmento_id:
        tipificaciones = Tipificacion.objects.filter(segmento_id=segmento_id).values('id', 'nombre')
        return JsonResponse(list(tipificaciones), safe=False)
    return JsonResponse({'error': 'segmento_id requerido'}, status=400)


def categorias(request):
    tipificacion_id = request.GET.get('tipificacion_id')
    if tipificacion_id:
        categorias = Categoria.objects.filter(tipificacion_id=tipificacion_id).values('id', 'nombre')
        return JsonResponse(list(categorias), safe=False)
    return JsonResponse({'error': 'tipificacion_id requerido'}, status=400)

def subcategorias(request):
    padre_id = request.GET.get('categoria_padre_id')
    if padre_id:
        subcategorias = Categoria.objects.filter(categoria_padre_id=padre_id).values('id', 'nombre')
        return JsonResponse(list(subcategorias), safe=False)
    return JsonResponse({'error': 'categoria_padre_id requerido'}, status=400)
