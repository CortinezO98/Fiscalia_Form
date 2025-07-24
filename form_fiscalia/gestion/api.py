from django.http import JsonResponse
from .models import *

def ciudadano(request):
    numero_identificacion = request.GET.get('numero_identificacion')
    if not numero_identificacion:
        return JsonResponse({'error': 'Número no enviado'}, status=400)

    try:
        ciu = Ciudadano.objects.get(numero_identificacion=numero_identificacion)
        return JsonResponse({
            'id': ciu.id,
            'nombre': ciu.nombre,
            'tipo_identificacion_id': ciu.tipo_identificacion_id,
            'correo': ciu.correo,
            'telefono': ciu.telefono,
            'direccion_residencia': ciu.direccion_residencia,
            'pais_id': ciu.pais_id,
            'ciudad': ciu.ciudad,
        })
    except Ciudadano.DoesNotExist:
        return JsonResponse({}, status=404)

def tipos_canal(request):
    """Obtener todos los tipos de canal"""
    tipos = TipoCanal.objects.all().values('id', 'nombre')
    return JsonResponse(list(tipos), safe=False)

def segmentos(request):
    """Obtener segmentos por tipo de canal"""
    tipo_canal_id = request.GET.get('tipo_canal_id')
    if not tipo_canal_id:
        return JsonResponse({'error': 'tipo_canal_id requerido'}, status=400)
    
    segmentos = Segmento.objects.filter(tipo_canal_id=tipo_canal_id).values(
        'id', 'nombre', 'tiene_segmento_ii'
    )
    return JsonResponse(list(segmentos), safe=False)

def segmentos_ii(request):
    """Obtener segmentos II por segmento"""
    segmento_id = request.GET.get('segmento_id')
    if not segmento_id:
        return JsonResponse({'error': 'segmento_id requerido'}, status=400)
    
    segmentos_ii = SegmentoII.objects.filter(segmento_id=segmento_id).values('id', 'nombre')
    return JsonResponse(list(segmentos_ii), safe=False)

def tipificaciones(request):
    """Obtener todas las tipificaciones (son universales)"""
    tipificaciones = Tipificacion.objects.all().values('id', 'nombre')
    return JsonResponse(list(tipificaciones), safe=False)

def categorias(request):
    """Obtener categorías por tipificación"""
    tipificacion_id = request.GET.get('tipificacion_id')
    if not tipificacion_id:
        return JsonResponse({'error': 'tipificacion_id requerido'}, status=400)
    
    categorias = Categoria.objects.filter(
        tipificacion_id=tipificacion_id,
        nivel=1  # Solo categorías de nivel 1
    ).values('id', 'nombre')
    return JsonResponse(list(categorias), safe=False)

def subcategorias(request):
    """Obtener subcategorías por categoría padre"""
    categoria_padre_id = request.GET.get('categoria_padre_id')
    if not categoria_padre_id:
        return JsonResponse({'error': 'categoria_padre_id requerido'}, status=400)
    
    subcategorias = Categoria.objects.filter(categoria_padre_id=categoria_padre_id).values('id', 'nombre')
    return JsonResponse(list(subcategorias), safe=False)

# Mantener compatibilidad con APIs antiguas (si es necesario)
def tipificaciones_old(request):
    """Para compatibilidad con código anterior"""
    segmento_id = request.GET.get('segmento_id')
    if segmento_id:
        tipificaciones = Tipificacion.objects.filter(segmento_id=segmento_id).values('id', 'nombre')
        return JsonResponse(list(tipificaciones), safe=False)
    return JsonResponse({'error': 'segmento_id requerido'}, status=400)

def categorias_old(request):
    """Para compatibilidad con código anterior"""
    tipificacion_id = request.GET.get('tipificacion_id')
    if tipificacion_id:
        categorias = Categoria.objects.filter(tipificacion_id=tipificacion_id).values('id', 'nombre')
        return JsonResponse(list(categorias), safe=False)
    return JsonResponse({'error': 'tipificacion_id requerido'}, status=400)