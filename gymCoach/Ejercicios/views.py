from django.shortcuts import render, redirect
from django.http import HttpResponse
from Ejercicios.models import Ejercicio
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

#READ
class EjercicioListview(ListView):
    model= Ejercicio
    context_object_name= "ejercicios"
    template_name= "Ejercicios/ejercicio_lista.html"


#DETAIL
class EjercicioDetailView(DetailView):
    model=Ejercicio    
    template_name="Ejercicios/ejercicio_detalle.html"

# CREATE
class EjercicioCreateview(CreateView):
    model= Ejercicio
    template_name= "Ejercicios/ejercicio_crear.html"
    success_url = reverse_lazy('ejercicios lista')
    fields=['nombre','descripcion', 'grupo_muscular']

#UPDATE
class EjercicioUpdateView(UpdateView):
    model= Ejercicio
    template_name= "Ejercicios/ejercicio_editar.html"
    success_url = reverse_lazy('ejercicios lista')
    fields=['nombre','descripcion','grupo_muscular']

#DELETE
class EjercicioDeleteView(DeleteView):
    model= Ejercicio
    template_name= "Ejercicios/ejercicio_eliminar.html"
    success_url = reverse_lazy('ejercicios lista')



