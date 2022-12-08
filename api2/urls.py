from django.urls import path
from . import views

urlpatterns = [
    path('tareas/', views.tareas),
    path('tareas/completar', views.completar_tarea)
]