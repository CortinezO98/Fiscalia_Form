from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import LoginForm
from django.http import HttpResponse


from django.shortcuts import redirect

def home_redirect_view(request):
    if request.user.is_authenticated:
        return redirect('home')  
    else:
        return render(request, 'usuarios/login.html')

    
def index(request):
    return render(request, 'usuarios/login.html')



def en_grupo(nombre):
    def check(user):
        return user.groups.filter(name=nombre).exists()
    return user_passes_test(check)

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
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
    return render(request, 'usuarios/login.html', {'form': form})

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
def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        rol = request.POST.get('rol')
        
        if username and password and rol:
            user = User.objects.create_user(username=username, password=password)
            grupo = Group.objects.get(name=rol)
            user.groups.add(grupo)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('crear_usuario')
    grupos = Group.objects.exclude(name='administrador')
    return render(request, 'usuarios/crear_usuario.html', {'grupos': grupos})

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


