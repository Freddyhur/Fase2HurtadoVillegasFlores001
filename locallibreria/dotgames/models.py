from django.db import models
from django.urls import reverse 
import uuid 

class Genero(models.Model):

    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Juego(models.Model):

    titulo = models.CharField(max_length=100)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID pal juego gei')
    descripcion = models.TextField(max_length=1000, help_text='Descripción del juego')
    autor = models.CharField(max_length=100)
    genero = models.ManyToManyField(Genero)

    def __str__(self):
        return self.titulo

    
    
