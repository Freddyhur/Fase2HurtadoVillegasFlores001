from django.shortcuts import render
from . models import Juego, Genero, Autor
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    return render(request, 'index.html')

