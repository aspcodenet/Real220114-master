from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators
from wtforms.fields import IntegerField, SelectField

class PersonEditForm(FlaskForm):
    name = StringField("name",[validators.Length(min=3, max=80, message="Skriv in mellan 2 och 80 tecken")])
    city = StringField("city",[validators.Length(min=5, max=30)])
    postalcode = IntegerField("postalcode",[validators.NumberRange(10000,99999)])
    pwd = StringField("pwd",[validators.Length(min=5, max=30), validators.EqualTo('pwdagain') ])
    pwdagain = StringField("pwdagain",[validators.Length(min=5, max=30)])
    position = SelectField("Spelar position", choices=[('g', 'Goalie'), ('d', 'Defence'), ('f', 'Forward')])    


class PersonNewForm(FlaskForm):
    name = StringField("name",[validators.Length(min=3, max=80, message="Skriv in mellan 2 och 80 tecken")])
    city = StringField("city",[validators.Length(min=5, max=30)])
    postalcode = IntegerField("postalcode",[validators.NumberRange(10000,99999)])
