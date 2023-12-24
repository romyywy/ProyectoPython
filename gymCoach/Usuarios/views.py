from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from Usuarios.forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from Usuarios.models import PerfilUsuario
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView



#log in
def login_request(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            
            login(request, user)
            return render(request, "index.html", {"mensaje": f'Bienvenido {user.username}'})
        else:
            return render(request, 'usuarios/login.html', {"formulario": formulario})
    
    else:
        formulario = AuthenticationForm()
        return render(request, "usuarios/login.html", {"formulario": formulario})


# registro de usuario (crear nuevo usuario con contraseña)  
def registro(request):
    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            formulario.save()
            return render(request,"index.html" ,  {"mensaje":"Usuario " + username + " registrado"})
        else:
            return render(request, 'usuarios/registro.html', {"formulario": formulario})

    else:
        formulario = CustomUserCreationForm()
        return render(request,"usuarios/registro.html" ,  {"formulario": formulario})


#esto es de prueba

#READ usuarios
class UsuarioListview(ListView):
    model= PerfilUsuario
    context_object_name= "usuarios"
    template_name= "usuarios/usuarios_lista.html"

#hasta aca va la prueba 
    

#logout
class Logoutview(LogoutView):
    template_name = "usuarios/logged_out.html"
    #next_page = reverse_lazy('principal')  # Redirect to the home page after logout


#a un usuario ya registrado, configurar su informacion
class PerfilUsuarioCreateView(LoginRequiredMixin, CreateView):
    model = PerfilUsuario
    template_name = "usuarios/crear_perfil.html"
    success_url = reverse_lazy("ver perfil")
    fields = ['usuario', 'imagen', 'rol']
    login_url = "/Usuarios/login"
    
class PerfilUsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = PerfilUsuario
    template_name = "usuarios/editar_perfil.html"
    success_url = reverse_lazy("ver perfil")
    fields = ['imagen', 'rol']
    login_url = "/Usuarios/login"

@login_required(login_url="login")
def perfil_usuario(request):
    try:
        request.user.perfil
        return render(request, "usuarios/perfil.html")
    except:
        return redirect("crear perfil")