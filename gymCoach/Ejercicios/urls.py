from django.urls import path
from Ejercicios.views import EjercicioCreateview,EjercicioDeleteView,EjercicioDetailView,EjercicioListview,EjercicioUpdateView


urlpatterns = [
    path('ejercicios_lista/',EjercicioListview.as_view(), name='ejercicios lista'),
    path('ejercicios_crear/',EjercicioCreateview.as_view(), name='ejercicios crear'),
    path('ejercicios_editar/<pk>',EjercicioUpdateView.as_view(), name='ejercicios editar'),
    path('ejercicios_eliminar/<pk>',EjercicioDeleteView.as_view(), name='ejercicios eliminar'),
    path('ejercicios_detalle/<pk>',EjercicioDetailView.as_view(), name='ejercicios detalle'),


]