from django.urls import path
from Usuarios.views import registro, login_request, LogoutView, PerfilUsuarioCreateView, PerfilUsuarioUpdateView, perfil_usuario, UsuarioListview


urlpatterns = [
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', registro, name='registro'),
    path('crear_perfil/', PerfilUsuarioCreateView.as_view(), name='crear perfil'),
    path('<pk>/editar_perfil/', PerfilUsuarioUpdateView.as_view(), name='editar perfil'),
    path('perfil_usuario/', perfil_usuario, name='ver perfil'),
    path('usuarios_lista/',UsuarioListview.as_view(), name='usuarios lista'),

]