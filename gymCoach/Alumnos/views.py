from django.shortcuts import render, redirect
from django.http import HttpResponse
from Alumnos.models import alumno
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoginRequiredMixin:
    @method_decorator(login_required)
    def dispatch(self, *args,**kwargs):
        return super().dispatch(*args,**kwargs)
    
# Base class for views with login_required
class LoginRequiredView(LoginRequiredMixin):
    pass



#READ
class AlumnoListview(LoginRequiredView,ListView):
    model= alumno
    context_object_name= "alumnos"
    template_name= "Alumnos/alumno_lista.html"


#DETAIL
class AlumnoDetailView(LoginRequiredView,DetailView):
    model=alumno    
    template_name="Alumnos/alumno_detalle.html"



# CREATE
class AlumnoCreateview(LoginRequiredView,CreateView):
    model= alumno
    template_name= "Alumnos/alumno_crear.html"
    success_url = reverse_lazy('alumnos lista')
    fields=['nombre','objetivo', 'ultima_rutina']

#UPDATE
class AlumnoUpdateView(LoginRequiredView,UpdateView):
    model= alumno
    template_name= "Alumnos/alumno_editar.html"
    success_url = reverse_lazy('alumnos lista')
    fields=['nombre','objetivo', 'ultima_rutina']

#DELETE
class AlumnoDeleteView(LoginRequiredView,DeleteView):
    model= alumno
    template_name= "Alumnos/alumno_eliminar.html"
    success_url = reverse_lazy('alumnos lista')



