"""Flask app for adopt app."""

import os
from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

PETFINDER_API_KEY = os.environ['PETFINDER_API_KEY']
PETFINDER_SECRET_KEY = os.environ['PETFINDER_SECRET_KEY']
API_TOKEN = os.environ['API_TOKEN']

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get("/")
def homepage():
    """Render page displaying a list of current users"""

    pets = Pet.query.all()
    return render_template("petlist.html", pets = pets)
    #rename html forms with _

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Display form to add a new pet; handle adding"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        #create pet
        new_pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {new_pet.name}!")
        return redirect("/")

    else:
        return render_template("addpetform.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """ Display pet details ; handle detail update form """

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)


    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash(f"{pet.name}'s record updated!")
        return redirect(f"/{pet.id}")

    else:
        return render_template("petinfo.html", pet = pet, form = form)

