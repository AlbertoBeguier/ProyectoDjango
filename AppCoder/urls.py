from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("agrega-curso/<nombre>/<camada>/", Curso),
    path("listar_cursos/", listar_cursos, name ="ListaCursos"),
    path("", inicio, name="Inicio"), 
    path("cursos/", cursos, name="Cursos"),
    path("profesores/", profesores, name="Profesores"),
    path("estudiantes/", estudiantes, name="Estudiantes"),
    path("entregables/", entregables, name="Entregables"),
    path("cursoFormulario/", cursoFormulario, name="cursoFormulario"),
    # registro del url de la vista busquedaCamada
    # para tener la capacidad de invocar la vista que va a renderizar
    # el formulario de búsqueda
    path("busquedaCamada/", busquedaCamada, name="busquedaCamada"),
    
    path("buscar/", buscar, name="buscar"),
    
]


