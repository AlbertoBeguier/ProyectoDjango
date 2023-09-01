from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("agrega-curso/<nombre>/<camada>/", Curso),
    path("listar_cursos/", listar_cursos),
    
    path("", inicio), # no se pone nada así siempre lee el inicio
    path("cursos/", cursos),
    path("profesores/", profesores),
    path("estudiantes/", estudiantes),
    path("entregables/", entregables),
    
]


