from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, IntegerField, FloatField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, URL

class PokemonForm(FlaskForm):
    number = IntegerField('Number', validators=[DataRequired()])
    attack = IntegerField('Attack', validators=[DataRequired()])
    defense = IntegerField('Defense', validators=[DataRequired()])
    imageURL = StringField('Image URL', validators=[DataRequired(), URL()])
    name = StringField('Name', validators=[DataRequired()])
    type = SelectField('Type', choices=[
  "fire",
  "electric",
  "normal",
  "ghost",
  "psychic",
  "water",
  "bug",
  "dragon",
  "grass",
  "fighting",
  "ice",
  "flying",
  "poison",
  "ground",
  "rock",
  "steel",
])
    moves = StringField('Moves', validators=[DataRequired()])
    encounterRate = FloatField('Encounter Rate')
    catchRate = FloatField('Catch Rate')
    captured = BooleanField('Captured')

class ItemForm(FlaskForm):
    happiness = IntegerField('Happiness')
    imageURL = StringField('Image URL', validators=[DataRequired(), URL()])
    name = StringField('Name', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])


