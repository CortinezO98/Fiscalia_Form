from django.shortcuts import render
from .models import Tipificacion
from django.http import HttpResponse
import csv

def buscar_tipificaciones(request):
    cedula = request.GET.get('cedula')
    tipificaciones = Tipificacion.objects.filter(cedula=cedula)
    return render(request, 'gestion/busqueda.html', {'tipificaciones': tipificaciones})

def exportar_csv(request):
    fecha_inicio = request.GET.get('inicio')
    fecha_fin = request.GET.get('fin')
    tipificaciones = Tipificacion.objects.filter(fecha__range=[fecha_inicio, fecha_fin])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporte.csv"'

    writer = csv.writer(response)
    writer.writerow(['Cédula', 'Agente', 'Descripción', 'Fecha'])
    for t in tipificaciones:
        writer.writerow([t.cedula, t.agente.username, t.descripcion, t.fecha])

    return response