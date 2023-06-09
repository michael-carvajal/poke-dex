from app.models import db, Pokemon
from sqlalchemy.sql import text

def seed_pokemons():
    pokemon1 = Pokemon(number = 1,
        imageUrl = '/images/pokemon_snaps/1.svg',
        name = 'Bulbasaur',
        attack = 49,
        defense = 49,
        typeId = 9,
        moves = ",".join([
          'tackle',
          'vine whip'
        ]),
        # moves = "tackle, vine whip",
        captured = True)
    pokemon2 = Pokemon(        number = 2,
        imageUrl = '/images/pokemon_snaps/2.svg',
        name = 'Ivysaur',
        attack = 62,
        defense = 63,
        typeId = 9,
        moves = ",".join([
          'tackle',
          'vine whip',
          'razor leaf'
        ]),
        # moves = "tackle, vine whip",
        captured = True)
    pokemon3 = Pokemon(        number = 3,
        imageUrl = '/images/pokemon_snaps/3.svg',
        name = 'Venusaur',
        attack = 82,
        defense = 83,
        typeId = 9,
        moves = ",".join([
          'tackle',
          'vine whip',
          'razor leaf'
        ]),
        # moves = "tackle, vine whip",
        captured = True)
    pokemon4 = Pokemon(        number = 4,
        imageUrl = '/images/pokemon_snaps/4.svg',
        name = 'Charmander',
        attack = 52,
        defense = 43,
        typeId = 1,
        moves = ",".join([
          'scratch',
          'ember',
          'metal claw'
        ]),
        # moves = "tackle, vine whip",
        captured = True)
    pokemon5 = Pokemon(        number = 5,
        imageUrl = '/images/pokemon_snaps/5.svg',
        name = 'Charmeleon',
        attack = 64,
        defense = 58,
        typeId = 1,
        moves = ",".join([
          'scratch',
          'ember',
          'metal claw',
          'flamethrower'
        ]),
        # moves = "tackle, vine whip",
        captured = True)

    all_pokemon = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5]
    add_pokemon = [db.session.add(pokemon) for pokemon in all_pokemon]
    db.session.commit()

def undo_pokemons():
    db.session.execute(text("DELETE FROM pokemons"))
    db.session.commit()
