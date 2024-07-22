from django.db import models

# Create your models here.
class Sanchez_Tucta_Persona(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    sexo = models.CharField(max_length=1)
    fecha_de_registro = models.DateTimeField(auto_now_add=True)
