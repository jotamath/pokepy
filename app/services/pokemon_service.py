import requests
from app.config.api_config import POKEAPI_BASE_URL

class PokemonService:
    @staticmethod
    def get_pokemon_by_name(name):
        try:
            response = requests.get(f"{POKEAPI_BASE_URL}/pokemon/{name}")
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Error fetching data from POKEAPI: {e}")
            return None
        