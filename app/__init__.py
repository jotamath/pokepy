from flask import Flask
from app.controllers.pokemon_controller import pokemon_controller
def create_app():
    app = Flask(__name__)

    app.register_blueprint(pokemon_controller)

    return app