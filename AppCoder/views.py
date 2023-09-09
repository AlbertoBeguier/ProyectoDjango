from django.shortcuts import render
from .models import Cursos
from django.http import HttpResponse, HttpRequest
from .forms import CursoFormulario

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

from .forms import CursoFormulario

def cursoFormulario(request): # va a trabajar sobre el modelo de Cursos
    
    if request.method == "POST":
        
        miFormulario = CursoFormulario(request.POST)
    
        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            
            curso=Cursos(nombre=data["curso"], camada=data["camada"], fecha_creacion=data["fecha_creacion"])
            curso.save()    
            return render(request, "inicio.html") 
    else:   
        miFormulario = CursoFormulario()
        return render(request, "cursoFormulario.html", {"miFormulario": miFormulario}) 
    
    
def busquedaCamada (request):
    # esta view renderiza (muestra en la web) el contenido del html
    return render (request, "busquedaCamada.html")

def buscar(request: HttpRequest):
    try: 
        if request.GET["camada"]:
            camada = request.GET["camada"]

            # para recuperar el curso que coincida con la camada
            curso = Cursos.objects.filter(camada__icontains=camada)
            return render(request, "resultadosBusqueda.html", {"curso": curso}) 
    except:
        return HttpResponse ("La camada buscada no existe")



