from django.db import models
from django.urls import reverse 
import uuid 

class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('autor-detail', args=[str(self.id)])

class Genero(models.Model):

    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Juego(models.Model):

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000, help_text='Descripción del juego')
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    genero = models.ManyToManyField(Genero)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('juego-detail', args=[str(self.id)])
    
