from django.urls import path
from Alumnos.views import AlumnoCreateview,AlumnoDeleteView,AlumnoDetailView,AlumnoListview,AlumnoUpdateView


urlpatterns = [
    path('alumnos_lista/',AlumnoListview.as_view(), name='alumnos lista'),
    path('alumnos_crear/',AlumnoCreateview.as_view(), name='alumnos crear'),
    path('alumnos_editar/<pk>',AlumnoUpdateView.as_view(), name='alumnos editar'),
    path('alumnos_eliminar/<pk>',AlumnoDeleteView.as_view(), name='alumnos eliminar'),
    path('alumnos_detalle/<pk>',AlumnoDetailView.as_view(), name='alumnos detalle'),


]