from flask import Flask, render_template,flash,redirect

from models import connect_db, db,Pet
from forms import AddPet
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLAlchemy_ECHO'] = True
app.config['SECRET_KEY'] = 'YOURSECRETISSAFEWITHME'
connect_db(app)
db.create_all()

@app.route('/')
def homepage():
    pets = Pet.query.all()
    return render_template('home.html',pets=pets)

@app.route('/add', methods = ["GET","POST"])
def add_pet():
    form=AddPet()
    if form.validate_on_submit():
        name=form.name.data
        species=form.species.data
        new_pet = Pet(name=name,species=species)
        db.session.add(new_pet)
        db.session.commit() 
        if form.photo.data:
            new_pet.photo_url = form.photo.data
            db.session.commit()
        if form.age.data:
            new_pet.age = form.age.data
            db.session.commit()      
        return redirect('/')
    else:
        return render_template('/pet-form.html',form=form)





@app.route('/<int:pet_id>',methods=["GET","POST"])
def show_pet(pet_id):
    pet = Pet.query.get(pet_id)
    form=AddPet(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        if form.photo.data:
            pet.photo_url = form.photo.data
            db.session.commit()
        if form.age.data:
            pet.age = form.age.data
        pet.available = form.available.data
        db.session.commit()
        return  redirect('/')
    else:
        return render_template('/pet_details.html',pet=pet,form=form)