from django.contrib import admin

from .models import Cursos,Profesor,Entregable,Estudiante

from datetime import datetime

admin.site.site_header= "Panel de Adm. AAB"

class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "camada","fecha_creacion","antiguedad")
    
    search_fields = ("nombre", "camada")
    
    list_filter = ("nombre", "camada")

    def antiguedad(self, object): # nombre objet por convencion
                                  # es el registro que realiza el cálculo
                                  # representa cada uno de los cursos
         if object.fecha_creacion: # si existe ese campo
             #retorne la antiguedad en días
             return (datetime.now().date() - object.fecha_creacion).days
         
         


# Register your models here.

admin.site.register(Cursos, CursoAdmin)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Entregable)

