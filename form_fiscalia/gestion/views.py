from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db import transaction
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.decorators.http import require_GET
from django.utils.timezone import make_aware, localtime
from usuarios.views import ValidarRolUsuario, en_grupo
from usuarios.enums import Roles
from .models import *
from io import BytesIO
from datetime import date, datetime
import openpyxl
from openpyxl.utils import get_column_letter
import inspect

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
        try:
            with transaction.atomic():
                cid = request.POST.get('cuidadano_id')
                if cid:
                    ciudadano = Ciudadano.objects.get(id=cid)
                    # Actualizar campos
                    ciudadano.tipo_identificacion_id = request.POST['tipo_identificacion']
                    ciudadano.numero_identificacion = request.POST['numero_identificacion']
                    ciudadano.nombre = request.POST['nombre']
                    ciudadano.correo = request.POST.get('correo', '')
                    ciudadano.telefono = request.POST.get('telefono', '')
                    ciudadano.direccion_residencia = request.POST.get('direccion_residencia', '')
                    ciudadano.pais_id = request.POST.get('pais') or None
                    ciudadano.ciudad = request.POST.get('ciudad', '')
                    ciudadano.save()
                else:
                    ciudadano = Ciudadano.objects.create(
                        tipo_identificacion_id=request.POST['tipo_identificacion'],
                        numero_identificacion=request.POST['numero_identificacion'],
                        nombre=request.POST['nombre'],
                        correo=request.POST.get('correo', ''),
                        telefono=request.POST.get('telefono', ''),
                        direccion_residencia=request.POST.get('direccion_residencia', ''),
                        pais_id=request.POST.get('pais') or None,
                        ciudad=request.POST.get('ciudad', '')
                    )

                Evaluacion.objects.create(
                    conversacion_id=request.POST['conversacion_id'],
                    observacion=request.POST['observacion'],
                    ciudadano=ciudadano,
                    categoria_id=request.POST.get('subcategoria') or request.POST['categoria'],
                    user=request.user
                )

                messages.success(request, "Evaluación guardada correctamente.")
        except Exception as e:
            RegistrarError(inspect.currentframe().f_code.co_name, str(e), request)
            messages.error(request, "Ocurrió un error al guardar la evaluación.")
        return redirect('index')

    tiposIdentificacion = TipoIdentificacion.objects.all()
    segmentos = Segmento.objects.all()
    paises = Pais.objects.all()

    if not tiposIdentificacion or not segmentos:
        messages.warning(request, "En este momento no es posible generar una tipificación. Por favor, contacte a soporte.")
        return redirect('index')

    return render(request, 'usuarios/evaluaciones/crear_evaluacion.html', {
        'tiposIdentificacion': tiposIdentificacion,
        'segmentos': segmentos,
        'paises': paises,
    })


@login_required
@en_grupo([Roles.ADMINISTRADOR.value, Roles.SUPERVISOR.value, Roles.AGENTE.value])
def buscar_tipificacion(request):
    """
    Busca Evaluacion(s) únicamente por numero_identificacion (ciudadano),
    paginadas de a 10. Devuelve todos los campos relacionados.
    """
    query = request.GET.get('q', '').strip()
    evaluaciones = Evaluacion.objects.none()

    if query:
        qs = (
            Evaluacion.objects
            .select_related(
                'ciudadano__tipo_identificacion',
                'categoria__tipificacion__segmento',
                'categoria__categoria_padre',
                'user'
            )
            .filter(ciudadano__numero_identificacion__icontains=query)
            .order_by('-fecha')
        )

        paginator = Paginator(qs, 10)
        page_number   = request.GET.get('page') or 1
        evaluaciones  = paginator.get_page(page_number)
    else:
        paginator = None

    return render(request, 'usuarios/evaluaciones/buscar_tipificacion.html', {
        'evaluaciones': evaluaciones,
        'paginator':    paginator,
        'page_obj':     evaluaciones,
        'is_paginated': evaluaciones.has_other_pages() if evaluaciones else False,
        'query':        query,
    })




@login_required
@en_grupo([Roles.ADMINISTRADOR.value, Roles.SUPERVISOR.value, Roles.AGENTE.value])
def reportes_view(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin    = request.GET.get('fecha_fin')

    qs = (
        Evaluacion.objects
        .select_related(
            'ciudadano__tipo_identificacion',
            'categoria__tipificacion__segmento',
            'categoria__categoria_padre',
            'user'
        )
        .order_by('-fecha')
    )

    if fecha_inicio and fecha_fin:
        try:
            fmt = '%Y-%m-%d'
            fi = make_aware(datetime.strptime(fecha_inicio, fmt))
            ff = make_aware(datetime.strptime(fecha_fin,    fmt))
            qs = qs.filter(fecha__range=(fi, ff))
        except ValueError:
            pass

    paginator = Paginator(qs, 10)
    page_obj  = paginator.get_page(request.GET.get('page') or 1)

    return render(request, 'usuarios/reportes.html', {
        'reportes':     page_obj,
        'paginator':    paginator,
        'page_obj':     page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'hoy':          date.today().isoformat(),
    })


@require_GET
@login_required
@en_grupo([Roles.ADMINISTRADOR.value, Roles.SUPERVISOR.value])
def exportar_excel(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin    = request.GET.get('fecha_fin')

    qs = (
        Evaluacion.objects
        .select_related(
            'ciudadano__tipo_identificacion',
            'categoria__tipificacion__segmento',
            'categoria__categoria_padre',
            'user'
        )
        .order_by('-fecha')
    )

    if fecha_inicio and fecha_fin:
        try:
            fmt = '%Y-%m-%d'
            fi = make_aware(datetime.strptime(fecha_inicio, fmt))
            ff = make_aware(datetime.strptime(fecha_fin,    fmt))
            qs = qs.filter(fecha__range=(fi, ff))
        except ValueError:
            pass


    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Reportes"
    headers = [
        'Fecha', 'Tipo Documento', 'Número ID', 'Nombre',
        'ID Conversación', 'Segmento','Tipificación','Categoría','Categoría Padre',
        'Observación','Usuario'
    ]
    for col, header in enumerate(headers, 1):
        ws.cell(row=1, column=col, value=header)

    for row_idx, ev in enumerate(qs.iterator(), start=2):
        ciu = ev.ciudadano
        cat = ev.categoria
        data = [
            localtime(ev.fecha).strftime('%Y-%m-%d %H:%M'),
            ciu.tipo_identificacion.nombre,
            ciu.numero_identificacion,
            ciu.nombre,
            ev.conversacion_id,
            cat.tipificacion.segmento.nombre if cat.tipificacion and cat.tipificacion.segmento else '',
            cat.tipificacion.nombre if cat.tipificacion else '',
            cat.nombre,
            cat.categoria_padre.nombre if cat.categoria_padre else '',
            ev.observacion,
            ev.user.username,
        ]
        for col, value in enumerate(data, 1):
            ws.cell(row=row_idx, column=col, value=value)

    for i, _ in enumerate(headers, 1):
        ws.column_dimensions[get_column_letter(i)].auto_size = True

    buffer = BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    resp = HttpResponse(
        buffer,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    resp['Content-Disposition'] = 'attachment; filename="reportes_tipificaciones.xlsx"'
    return resp