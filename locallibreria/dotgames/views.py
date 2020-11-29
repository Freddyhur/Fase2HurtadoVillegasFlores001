from django.shortcuts import render
from . models import Juego, Genero, Autor
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def index(request):
    return render(request, 'index.html')

class PotoListView(generic.ListView):
    model = Juego    
    template_name = 'index.html'
    paginate_by = 10

class JuegoListView(generic.ListView):
    model = Juego
    paginate_by = 10
    
class JuegoDetailView(generic.DetailView):
    model = Juego

class AutorCreate(CreateView):
    model = Autor
    fields = '__all__'
    initial ={'nombre': ''}

class AutorUpdate(UpdateView):
    model = Autor
    fields = ['nombre']

class AutorDelete(DeleteView):
    model = Autor
    success_url = reverse_lazy('autor')


class AutorDetailView(generic.DetailView):
    model=Autor

class AutorListView(generic.ListView):
    model = Autor
    paginate_by = 10