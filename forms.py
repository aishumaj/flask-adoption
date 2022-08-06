"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """Form for adding pets for adoption"""

    name = StringField("Pet Name",
        validators = [InputRequired()])
    species = SelectField("Species",
        choices = [("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL",
        validators= [Optional(), URL()])
    age = SelectField("Age",
        choices = [("baby", "Baby"), ("young", "Young"), ("adult", "Adult"),
        ("senior", "Senior")])
    notes = StringField("Additional Information",
        validators = [Optional()])
        #pass in max length



class EditPetForm(FlaskForm):
    """Form for adding pets for adoption"""

    photo_url = StringField("Photo URL",
        validators= [Optional(), URL()])
    notes = StringField("Additional Information",
        validators = [Optional()])
        # pass in max length
    available = BooleanField("Is this pet available?")