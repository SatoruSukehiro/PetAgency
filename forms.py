from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms.fields.core import BooleanField, IntegerField, RadioField, SelectField, StringField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import URL, Length, NumberRange , Optional




class AddPet(FlaskForm):
    name=StringField('Name',validators=[Length(min=1,max=20,message="Sorry Name is Too Long")])
    species=SelectField('Species',choices=[('cat','Cat'),('dog',"Dog"),('porcupine',"Porcupine")])
    photo=StringField('PhotoUrl',validators=[Optional(),URL()])
    age=IntegerField('Age',validators=[Optional(),NumberRange(min=1, max=30,message="Age must be between 1-30")])
    notes=TextAreaField('Notes')
    available = BooleanField('Avaliable?')
