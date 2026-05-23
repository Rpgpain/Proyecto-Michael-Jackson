from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Album

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def crear_usuarios_defecto():
    """Asegura la existencia de los dos usuarios de prueba."""
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    if not User.objects.filter(username='usuario').exists():
        User.objects.create_user('usuario', 'usuario@example.com', 'usuario123')

def login_view(request):
    crear_usuarios_defecto()
    
    # Si ya está autenticado, redirigir a legado
    if request.user.is_authenticated:
        return redirect('legado')
        
    error_msg = None
    if request.method == 'POST':
        usuario_input = request.POST.get('username')
        clave_input = request.POST.get('password')
        
        user = authenticate(request, username=usuario_input, password=clave_input)
        if user is not None:
            auth_login(request, user)
            next_url = request.GET.get('next', 'legado')
            return redirect(next_url)
        else:
            error_msg = "Credenciales incorrectas. Inténtalo de nuevo."
            
    return render(request, 'login.html', {'error': error_msg})

def logout_view(request):
    auth_logout(request)
    return redirect('inicio')

@login_required
def legado(request):
    return render(request, 'index2.html')

@login_required
def albumes(request):
    albumes_list = Album.objects.all().order_by('anio_lanzamiento')
    return render(request, 'index3.html', {'albumes': albumes_list})