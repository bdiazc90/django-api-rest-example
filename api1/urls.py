from django.urls import path
from . import views

urlpatterns = [
    path('pais/', views.pais)
]