from app.models import db, Item
from sqlalchemy.sql import text
from random import choice

def random_image():
    images = [
    "/images/pokemon_berry.svg",
    "/images/pokemon_egg.svg",
    "/images/pokemon_potion.svg",
    "/images/pokemon_super_potion.svg",
  ]
    image = choice(images)
    return image

def seed_items():
    item1 = Item(happiness = 25, name = 'Fantastic Plastic Computer', imageUrl = random_image(), price =  10, pokemonId = 1)
    item2 = Item(happiness = 50, name = 'Ergonomic Rubber Hat', imageUrl = random_image(), price =  20, pokemonId = 2)
    item3 = Item(happiness = 30, name = 'Refined Rubber Shoes', imageUrl = random_image(), price =  12, pokemonId = 3)
    item4 = Item(happiness = 35, name = 'Intelligent Plastic Gloves', imageUrl = random_image(), price =  70, pokemonId = 4)
    item5 = Item(happiness = 85, name = 'Practical Soft Sausages', imageUrl = random_image(), price =  60, pokemonId = 5)

    all_items = [item1, item2, item3, item4, item5]
    add_items = [db.session.add(item) for item in all_items]
    db.session.commit()

def undo_items():
    db.session.execute(text("DELETE FROM items"))
    db.session.commit()
