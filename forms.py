from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators
from wtforms.fields import IntegerField

class PersonEditForm(FlaskForm):
    name = StringField("name",[validators.Length(min=3, max=80, message="Skriv in mellan 2 och 80 tecken")])
    city = StringField("city",[validators.Length(min=5, max=30)])
    postalcode = IntegerField("postalcode",[validators.NumberRange(10000,99999)])

