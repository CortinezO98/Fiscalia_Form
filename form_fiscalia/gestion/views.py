from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from usuarios.views import ValidarRolUsuario, en_grupo
from usuarios.enums import Roles
from .models import *

def index(request):
    if request.user.is_authenticated:
        if ValidarRolUsuario(request, Roles.ADMINISTRADOR.value):
            return redirect('dashboard_admin')
        elif ValidarRolUsuario(request, Roles.SUPERVISOR.value):
            return redirect('dashboard_supervisor')
        elif ValidarRolUsuario(request, Roles.AGENTE.value):
            return redirect('dashboard_agente')
        
        messages.warning(request, "Usted no esta autorizado.")
        return redirect('logout')
    else:
        return redirect('login')


@login_required
@en_grupo([Roles.ADMINISTRADOR.value, Roles.SUPERVISOR.value, Roles.AGENTE.value])
def crear_evaluacion(request):
    if request.method == 'POST':
        # Aquí iría la lógica para crear una evaluación
        pass
    
    context = {
        "tiposIdentificacion": TipoIdentificacion.objects.all(),
        "segmentos": Segmento.objects.all(),
    }

    return render(request, 'usuarios/evaluaciones/crear_evaluacion.html', context)


@login_required
# @en_grupo([Roles.ADMINISTRADOR.value, Roles.SUPERVISOR.value, Roles.AGENTE.value])
def buscar_tipificacion(request):

    query = request.GET.get('q', '').strip()
    tipificaciones = Tipificacion.objects.none()

    if query:
        tipificaciones = Tipificacion.objects.filter(
            Q(evaluacion__ciudadano__numero_identificacion__icontains=query) |
            Q(evaluacion__ciudadano__nombre__icontains=query) |
            Q(evaluacion__id_conversacion__icontains=query)
        ).select_related('evaluacion__ciudadano', 'opcion').order_by('-fecha_registro')

        paginator = Paginator(tipificaciones, 10)
        page_number = request.GET.get('page')
        tipificaciones = paginator.get_page(page_number)

    return render(request, 'usuarios/evaluaciones/buscar_tipificacion.html', {
        'tipificaciones': tipificaciones
    })


@login_required
# @en_grupo([Roles.ADMINISTRADOR.value, Roles.SUPERVISOR.value])
def reportes_view(request):

    # reportes = Tipificacion.objects.all()
    # fecha_inicio = request.GET.get('fecha_inicio')
    # fecha_fin = request.GET.get('fecha_fin')

    # if fecha_inicio and fecha_fin:
    #     reportes = reportes.filter(fecha_registro__date__range=[fecha_inicio, fecha_fin])

    return render(request, 'usuarios/reportes.html', {})


@login_required
# @en_grupo([Roles.ADMINISTRADOR.value, Roles.SUPERVISOR.value])
def exportar_csv(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    reportes = Tipificacion.objects.select_related('evaluacion__ciudadano', 'opcion').all()

    if fecha_inicio and fecha_fin:
        try:
            fi = make_aware(datetime.strptime(fecha_inicio, '%Y-%m-%d'))
            ff = make_aware(datetime.strptime(fecha_fin, '%Y-%m-%d'))
            reportes = reportes.filter(fecha_registro__range=[fi, ff])
        except ValueError:
            pass  

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporte_tipificaciones.csv"'

    writer = csv.writer(response)
    writer.writerow(['Fecha Registro', 'Ciudadano', 'Documento', 'ID Conversación', 'Opción', 'Valor', 'Observaciones'])

    for r in reportes:
        writer.writerow([
            r.fecha_registro.strftime('%Y-%m-%d %H:%M'),
            r.evaluacion.ciudadano.nombre,
            r.evaluacion.ciudadano.numero_identificacion,
            r.evaluacion.id_conversacion,
            r.opcion.texto if r.opcion else '',
            r.valor,
            r.observaciones
        ])

    return response