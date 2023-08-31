from django.shortcuts import render
from .models import Cursos
from django.http import HttpResponse

# Create your views here.

def Curso(request, nombre, camada):
   
    curso=Cursos(nombre=nombre, camada=camada)
    curso.save()
    return HttpResponse (f"""
<p> Curso:{curso.nombre} - Camada:{curso.camada} creado con éxito!</p>
""") 

def listar_cursos(request):
    # tengo que hacer una consulta a la base de datos
    # para recuperar información (leer informacio de la  BD)
    # estas consultas se encuentran dentro de los denominados 
    # manager de los modelos de Django
    lista = Cursos.objects.all() # traeme todos los cursos (all) de la clase Cursos 

    return render(request, "lista_cursos.html",{"lista_cursos": lista})
    # el método render recibe obligatoriamente --> request,
    # --> el html que quiero renderizar (creo una carpeta con ese html)
    # --> el contexto



