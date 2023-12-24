from django.shortcuts import render, redirect
from django.http import HttpResponse
from Ejercicios.models import Ejercicio
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# mixin class with login required decorator 

class LoginRequiredMixin:
    @method_decorator(login_required)
    def dispatch(self, *args,**kwargs):
        return super().dispatch(*args,**kwargs)
    
# Base class for views with login_required
class LoginRequiredView(LoginRequiredMixin):
    pass



#READ
class EjercicioListview(LoginRequiredView,ListView):
    model= Ejercicio
    context_object_name= "ejercicios"
    template_name= "Ejercicios/ejercicio_lista.html"


#DETAIL
class EjercicioDetailView(LoginRequiredView,DetailView):
    model=Ejercicio    
    template_name="Ejercicios/ejercicio_detalle.html"

# CREATE
class EjercicioCreateview(LoginRequiredView,CreateView):
    model= Ejercicio
    template_name= "Ejercicios/ejercicio_crear.html"
    success_url = reverse_lazy('ejercicios lista')
    fields=['nombre','descripcion', 'grupo_muscular']

#UPDATE
class EjercicioUpdateView(LoginRequiredView,UpdateView):
    model= Ejercicio
    template_name= "Ejercicios/ejercicio_editar.html"
    success_url = reverse_lazy('ejercicios lista')
    fields=['nombre','descripcion','grupo_muscular']

#DELETE
class EjercicioDeleteView(LoginRequiredView,DeleteView):
    model= Ejercicio
    template_name= "Ejercicios/ejercicio_eliminar.html"
    success_url = reverse_lazy('ejercicios lista')



