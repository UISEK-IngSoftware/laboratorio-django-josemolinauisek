from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pokemons, name='lista_pokemons'),
    path('pokemon/<int:pokemon_id>/', views.detalle_pokemon, name='detalle_pokemon'),
]
