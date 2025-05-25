from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import static
from .models import Pokemon
from django.shortcuts import render, get_object_or_404

def lista_pokemons(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'index.html', {'pokemons': pokemons})

def detalle_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    return render(request, 'detalle.html', {'pokemon': pokemon})
