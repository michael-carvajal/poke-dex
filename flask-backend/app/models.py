from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pokemon(db.Model):
    __tablename__ = "pokemons"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    imageURL = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False, unique=True)
    typeId = db.Column(db.Integer, db.ForeignKey("pokemontypes.id"), nullable=False)
    moves = db.Column(db.String, nullable=False)
    # moves is weird...
    encounterRate = db.Column(db.Float)
    catchRate = db.Column(db.Float)
    captured = db.Column(db.Boolean)

    items = db.Relationship("Item", back_populates="pokemon")
    type = db.Relationship("PokemonType", back_populates="pokemons")

    def to_dict(self):
        return {
            "id": self.id,
            "number": self.number,
            "attack": self.attack,
            "defense": self.defense,
            "imageURL": self.imageURL,
            "name": self.name,
            "typeId": self.typeId,
            "moves": self.moves,
        }


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    happiness = db.Column(db.Integer)
    imageURL = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    pokemonId = db.Column(db.Integer, db.ForeignKey("pokemons.id"), nullable=False)

    pokemon = db.Relationship("Pokemon", back_populates="items")

    def to_dict(self):
        return {
            "id": self.id,
            "happiness": self.happiness,
            "imageURL": self.imageURL,
            "name": self.name,
            "price": self.price,
        }

    pokemonId = db.Column(db.Integer, db.ForeignKey("pokemons.id"), nullable=False)


class PokemonType(db.Model):
    __tablename__ = "pokemontypes"

    id = db.Column(db.Integer, primary_key=True)
    types = db.Column(db.String, nullable=False)

    pokemons = db.Relationship("Pokemon", back_populates="type")

    def to_dict(self):
        return {"id": self.id, "types": self.types}
