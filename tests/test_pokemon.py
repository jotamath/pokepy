import pytest
from app.services.pokemon_service import PokemonService

def test_get_pokemon_by_name():
    pokemon = PokemonService.get_pokemon_by_name('pikachu')
    assert pokemon is not None
    assert pokemon['name'] == 'pikachu'
