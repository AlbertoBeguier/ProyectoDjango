from django.db import models 

 
class Cursos(models.Model): 

    nombre = models.CharField(max_length=40) 
    camada = models.IntegerField() 
    fecha_creacion = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.camada}"
    
    class Meta(): 
        verbose_name = "curso" 
        ordering = ("nombre", "-camada")
        
        # debe ser una tupla
        unique_together = ("nombre", "camada")
         
        
        
        

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre}  {self.apellido}"
    
    
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    
    cursos = models.ManyToManyField(Cursos)
    
    def __str__(self):
        return f"{self.nombre}  {self.apellido}"
    
    class Meta(): 
       verbose_name = "profesor"
       verbose_name_plural = "profesores"
       
       
    
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.fechaDeEntrega} - {self.entregado}"



    