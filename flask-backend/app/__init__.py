from flask import Flask
from flask_migrate import Migrate
from .config import Configuration
from .models import db, Pokemon, PokemonType, Item
from .seed import seed_commands
# import statement for CSRF
from flask_wtf.csrf import CSRFProtect, generate_csrf
import os


app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
Migrate(app, db)
app.cli.add_command(seed_commands)

@app.route('/api/pokemon')
def home():
    pokemons = [pokemon.to_dict() for pokemon in Pokemon.query.all()]
    return pokemons

@app.route('/api/pokemon/<int:id>')
def pokemon_detail(id):
    pokemon = Pokemon.query.get(id)
    type = PokemonType.query.get(pokemon['typeId'])
    print(type)
    return pokemon.to_dict()

# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response
