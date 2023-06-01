from flask.cli import AppGroup
from .types import seed_types, undo_types
from .items import seed_items, undo_items
from .pokemons import seed_pokemons, undo_pokemons

seed_commands = AppGroup('seed')

@seed_commands.command('all')
def seed():
    seed_pokemons()
    seed_items()
    seed_types()
    print('All seeds created!')

@seed_commands.command('undo')
def undo():
    undo_pokemons()
    undo_items()
    undo_types()
    print('All seeds destroyed!')
