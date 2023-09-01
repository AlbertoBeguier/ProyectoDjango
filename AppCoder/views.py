from django.shortcuts import render
from .models import Cursos
from django.http import HttpResponse

def Curso(request, nombre, camada):
   
    curso=Cursos(nombre=nombre, camada=camada)
    curso.save()
    return HttpResponse (f"""
<p> Curso:{curso.nombre} - Camada:{curso.camada} creado con éxito!</p>
""") 

def listar_cursos(request):
    lista = Cursos.objects.all() 
    return render(request, "lista_cursos.html",{"lista_cursos": lista})
    

def inicio(request):
    return render(request, "inicio.html") 

def cursos(request):
    return render(request, "cursos.html") 

def profesores(request):
    return render(request, "profesores.html")  

def estudiantes(request):
     return render(request, "estudiantes.html")  

def entregables(request):
    return render(request, "entregables.html")  




