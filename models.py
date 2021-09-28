from flask_sqlalchemy import SQLAlchemy





db = SQLAlchemy()
def connect_db(app):
    '''Connects Database to Server'''
    db.app=app
    db.init_app(app)



class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.String(20),
                     nullable=False)
    species = db.Column(db.String(25),
                     nullable=False)
    photo_url = db.Column(db.String,
                            default = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcloud.mysteryscience.com%2Fimage%2Ffetch%2Fhttps%3A%2F%2Fwww.dropbox.com%2Fs%2Fp5egi6wo4wfoqt4%2FThumbnail-M1-AnimalAdventures-SMALL-grey.jpg%253Fdl%253D1&f=1&nofb=1")
    age = db.Column(db.Integer)
    notes = db.Column(db.String())
    available = db.Column(db.Boolean, default=True)