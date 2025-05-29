from django.shortcuts import render, get_object_or_404
from .models import Pokemon

def lista_pokemons(request):
    query = request.GET.get('q', '')
    if query:
        pokemons = Pokemon.objects.filter(nombre__icontains=query)
    else:
        pokemons = Pokemon.objects.all()
    return render(request, 'index.html', {'pokemons': pokemons})

def detalle_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    return render(request, 'detalle_pokemon.html', {'pokemon': pokemon})
