from django.contrib.auth.models import User, Group
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import *
from django.http import HttpResponse
from django.core.paginator import  Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
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



from django.shortcuts import redirect

def home_redirect_view(request):
    if request.user.is_authenticated:
        return redirect('home')  
    else:
        return render(request, 'usuarios/auth/login.html')

    
def index(request):
    return render(request, 'usuarios/auth/login.html')



def en_grupo(nombre):
    def check(user):
        return user.groups.filter(name=nombre).exists()
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
                if user.groups.filter(name='administrador').exists():
                    return redirect('dashboard_admin')
                elif user.groups.filter(name='supervisor').exists():
                    return redirect('dashboard_supervisor')
                elif user.groups.filter(name='agente').exists():
                    return redirect('dashboard_agente')
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
@en_grupo('agente')
def dashboard_agente(request):
    return render(request, 'usuarios/dashboard_agente.html')

@login_required
@en_grupo('supervisor')
def dashboard_supervisor(request):
    return render(request, 'usuarios/dashboard_supervisor.html')

@login_required
@en_grupo('administrador')
def dashboard_admin(request):
    return render(request, 'usuarios/dashboard_admin.html')



@login_required
@en_grupo('administrador')
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
@en_grupo('administrador')
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

    # Paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(usuarios_list, 10)  # 10 usuarios por página

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
@en_grupo('administrador')
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
@en_grupo('administrador')
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
@en_grupo('administrador')
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
def reportes_view(request):
    from .models import Tipificacion
    reportes = Tipificacion.objects.all()
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    if fecha_inicio and fecha_fin:
        reportes = reportes.filter(fecha__range=[fecha_inicio, fecha_fin])
    return render(request, 'usuarios/reportes.html', {'reportes': reportes})

def buscar_tipificaciones(request):
    return HttpResponse("Vista buscar_tipificaciones aún no implementada")


def exportar_csv(request):
    return HttpResponse("Vista EXPORTAR_CSV aún no implementada")


