from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('juego/', views.JuegoListView.as_view(), name='juego'),
    path('juego/<int:pk>', views.JuegoDetailView.as_view(), name='juego-detail'),

     

]



