from django.urls import path
from . import views

urlpatterns = [
    path('', views.PotoListView.as_view(), name='index'),
    path('juego/', views.JuegoListView.as_view(), name='juego'),
    path('juego/<int:pk>', views.JuegoDetailView.as_view(), name='juego-detail'),
    path('autor/<int:pk>', views.AutorDetailView.as_view(), name='autor-detail'),
    path('autor/', views.AutorListView.as_view(), name='autor'),
    path('poto/', views.PotoListView.as_view(), name='poto')
     
]


urlpatterns+=[
    path('autor/create/', views.AutorCreate.as_view(), name='autor_create'),
    path('autor/<int:pk>/update/', views.AutorUpdate.as_view(), name='autor_update'),
    path('autor/<int:pk>/delete/', views.AutorDelete.as_view(), name='autor_delete'),
    
]


