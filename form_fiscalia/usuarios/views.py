from django.contrib.auth.models import User, Group
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import *
from django.http import HttpResponse
from django.core.paginator import  Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .decorators import en_grupo  
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q
from .models import *
from django.utils import timezone
from django.http import HttpResponseForbidden
from django.utils.timezone import make_aware
from django.utils.timezone import now, localtime
from django.db.models import Count
from datetime import datetime
from django.shortcuts import redirect
from .enums import Roles

def home_redirect_view(request):
    if request.user.is_authenticated:
        return redirect('home')  
    else:
        return render(request, 'usuarios/auth/login.html')


def en_grupo(roles_id):
    def check(user):
        for rol_id in roles_id:
            if user.groups.filter(id=rol_id).exists():
                return True
    return user_passes_test(check)



def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Credenciales incorrectas. Intenta nuevamente.")
        else:
            messages.error(request, "Captcha incorrecto. Intenta nuevamente.")
    return render(request, 'usuarios/auth/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
@en_grupo([Roles.AGENTE.value])
def dashboard_agente(request):


    context = {
        
    }
    
    return render(request, 'usuarios/dashboard_agente.html', context)






@login_required
@en_grupo([Roles.SUPERVISOR.value])
def dashboard_supervisor(request):
    # agentes_activos = Agente.objects.filter(activo=True).count() 
    # total_evaluaciones = Evaluacion.objects.count()
    # evaluaciones_hoy = Evaluacion.objects.filter(fecha_creacion__date=localtime(now()).date()).count()
    # eficiencia = round((evaluaciones_hoy / agentes_activos * 100), 2) if agentes_activos > 0 else 0.0

    context = {
        # 'total_evaluaciones': total_evaluaciones,
        # 'evaluaciones_hoy': evaluaciones_hoy,
        # 'agentes_activos': agentes_activos,
        # 'eficiencia': eficiencia
    }
    return render(request, 'usuarios/dashboard_supervisor.html', context)




@login_required
@en_grupo([Roles.ADMINISTRADOR.value])
def dashboard_admin(request):
    return render(request, 'usuarios/dashboard_admin.html')


@login_required
@en_grupo([Roles.ADMINISTRADOR.value])
def crear_usuario(request, user_id=None):
    user = get_object_or_404(User, id=user_id) if user_id else None
    grupos = Group.objects.all()
    grupo_asignado = user.groups.first() if user else None

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        rol_id = request.POST.get("rol", "")
        is_active = request.POST.get("is_active") == "on"

        errors = []
        
        required_fields = {
            'username': username,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'rol': rol_id
        }
        
        if not user: 
            required_fields['password'] = password
            required_fields['confirm_password'] = confirm_password

        for field, value in required_fields.items():
            if not value:
                errors.append(f"El campo {field.replace('_', ' ')} es requerido.")

        if password or confirm_password:
            if password != confirm_password:
                errors.append("Las contraseñas no coinciden.")
            elif len(password) < 8:
                errors.append("La contraseña debe tener al menos 8 caracteres.")

        if User.objects.filter(username=username).exclude(pk=user.pk if user else None).exists():
            errors.append("El nombre de usuario ya está en uso.")
            
        if User.objects.filter(email=email).exclude(pk=user.pk if user else None).exists():
            errors.append("El correo electrónico ya está en uso.")

        if email and '@' not in email:
            errors.append("Ingrese un correo electrónico válido.")

        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'usuarios/auth/crear_usuario.html', {
                'user': user,
                'grupos': grupos,
                'grupo_asignado': grupo_asignado
            })

        # Crear o actualizar el usuario
        try:
            grupo = Group.objects.get(id=rol_id)
            
            if not user:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    is_active=is_active
                )
            else:
                user.username = username
                user.email = email
                user.first_name = first_name
                user.last_name = last_name
                user.is_active = is_active
                if password:
                    user.set_password(password)
                user.save()

            user.groups.clear()
            user.groups.add(grupo)
            
            grupo_nombre = grupo.name.lower()

            if grupo_nombre == "agente":
                from .models import Agente
                Agente.objects.get_or_create(user=user, defaults={
                    "nombre": f"{user.first_name} {user.last_name}"
                })

            elif grupo_nombre == "supervisor":
                from .models import Supervisor
                Supervisor.objects.get_or_create(user=user, defaults={
                    "nombre": f"{user.first_name} {user.last_name}"
                })

            elif grupo_nombre == "administrador":
                from .models import Administrador
                Administrador.objects.get_or_create(user=user, defaults={
                    "nombre": f"{user.first_name} {user.last_name}"
                })

            messages.success(request, f"Usuario {'actualizado' if user_id else 'creado'} correctamente.")
            return redirect('dashboard_admin')

        except Exception as e:
            messages.error(request, f"Error al {'actualizar' if user_id else 'crear'} el usuario: {str(e)}")
            return render(request, 'usuarios/auth/crear_usuario.html', {
                'user': user,
                'grupos': grupos,
                'grupo_asignado': grupo_asignado
            })

    return render(request, 'usuarios/auth/crear_usuario.html', {
        'user': user,
        'grupos': grupos,
        'grupo_asignado': grupo_asignado
    })





@login_required
@en_grupo([Roles.ADMINISTRADOR.value])
def ver_usuarios(request):
    query = request.GET.get('q', '').strip()
    usuarios_list = User.objects.all().order_by('username')

    if query:
        search_terms = query.split()
        q_objects = Q()
        for term in search_terms:
            q_objects |= Q(username__icontains=term)
            q_objects |= Q(first_name__icontains=term)
            q_objects |= Q(last_name__icontains=term)
            q_objects |= Q(email__icontains=term)
        usuarios_list = usuarios_list.filter(q_objects).distinct()

    page = request.GET.get('page', 1)
    paginator = Paginator(usuarios_list, 10)  

    try:
        usuarios = paginator.page(page)
    except PageNotAnInteger:
        usuarios = paginator.page(1)
    except EmptyPage:
        usuarios = paginator.page(paginator.num_pages)

    context = {
        'usuarios': usuarios,
        'query': query,
        'paginator': paginator,
        'start_index': usuarios.start_index(),
        'end_index': usuarios.end_index(),
    }

    return render(request, 'usuarios/auth/ver_usuarios.html', context)


@login_required
@en_grupo([Roles.ADMINISTRADOR.value])
@require_POST
def toggle_user_status(request, user_id):
    try:
        usuario = User.objects.get(id=user_id)
        usuario.is_active = not usuario.is_active
        usuario.save()
        return JsonResponse({'success': True})
    except User.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Usuario no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

@login_required
@en_grupo([Roles.ADMINISTRADOR.value])
def eliminar_usuario(request, user_id):
    try:
        usuario = User.objects.get(id=user_id)
        usuario.delete()
        messages.success(request, f'Usuario {usuario.username} eliminado correctamente')
        return redirect('ver_usuarios')
    except User.DoesNotExist:
        messages.error(request, 'El usuario no existe')
        return redirect('ver_usuarios')
    except Exception as e:
        messages.error(request, f'Error al eliminar usuario: {str(e)}')
        return redirect('ver_usuarios')









@login_required
@en_grupo([Roles.ADMINISTRADOR.value])
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)

    if request.method == 'POST':
        usuario.first_name = request.POST.get('first_name', usuario.first_name)
        usuario.last_name = request.POST.get('last_name', usuario.last_name)
        usuario.email = request.POST.get('email', usuario.email)
        usuario.save()
        messages.success(request, 'Usuario actualizado correctamente')
        return redirect('ver_usuarios')

    return render(request, 'usuarios/editar_usuario.html', {'usuario': usuario})








@login_required
@en_grupo([Roles.ADMINISTRADOR.value, Roles.SUPERVISOR.value, Roles.AGENTE.value])
def crear_evaluacion(request):
    if request.method == 'POST':
        # Aquí iría la lógica para crear una evaluación
        pass
    else:
        # Aquí iría la lógica para mostrar el formulario de creación de evaluación
        pass

    return render(request, 'usuarios/evaluaciones/crear_evaluacion.html')




@login_required
@en_grupo([Roles.ADMINISTRADOR.value, Roles.SUPERVISOR.value, Roles.AGENTE.value])
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
@en_grupo([Roles.ADMINISTRADOR.value, Roles.SUPERVISOR.value])
def reportes_view(request):

    # reportes = Tipificacion.objects.all()
    # fecha_inicio = request.GET.get('fecha_inicio')
    # fecha_fin = request.GET.get('fecha_fin')

    # if fecha_inicio and fecha_fin:
    #     reportes = reportes.filter(fecha_registro__date__range=[fecha_inicio, fecha_fin])

    return render(request, 'usuarios/reportes.html', {})



@login_required
@en_grupo([Roles.ADMINISTRADOR.value, Roles.SUPERVISOR.value])
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

def ValidarRolUsuario(request, rol_id):
    user = request.user
    return user.groups.filter(id=rol_id).exists()
