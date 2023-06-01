from app.models import db, PokemonType
from sqlalchemy.sql import text

def seed_types():
    type1 = PokemonType(types='fire')
    type2 = PokemonType(types='electric')
    type3 = PokemonType(types='normal')
    type4 = PokemonType(types='ghost')
    type5 = PokemonType(types='psychic')
    type6 = PokemonType(types='water')
    type7 = PokemonType(types='bug')
    type8 = PokemonType(types='dragon')
    type9 = PokemonType(types='grass')
    type10 = PokemonType(types='fighting')
    type11 = PokemonType(types='ice')
    type12 = PokemonType(types='flying')
    type13 = PokemonType(types='poison')
    type14 = PokemonType(types='ground')
    type15 = PokemonType(types='rock')
    type16 = PokemonType(types='steel')

    all_types = [type1, type2, type3, type4, type5, type6, type7, type8, type9, type10, type11, type12, type13, type14, type15, type16]
    add_types = [db.session.add(type) for type in all_types]
    db.session.commit()

def undo_types():
    db.session.execute(text("DELETE FROM pokemontypes"))
    db.session.commit()


