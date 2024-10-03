from flask import Blueprint, render_template, request
from app.services.pokemon_service import PokemonService

pokemon_controller = Blueprint('pokemon_controller', __name__)

@pokemon_controller.route('/')
def index():
    return render_template('index.html')

@pokemon_controller.route('/pokemon', methods=['GET'])
def get_pokemon():
    pokemon_name = request.args.get('name')
    if not pokemon_name:
        return render_template('index.html', error="Pokémon not found")
    
    pokemon_data = PokemonService.get_pokemon_by_name(pokemon_name)
    if not pokemon_data:
        return render_template('index.html', error="Pokémon not found")
    
    return render_template('pokemon.html', pokemon=pokemon_data)

 