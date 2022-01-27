from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators
from wtforms.fields import IntegerField, SelectField, BooleanField



class UserRegistrationForm(FlaskForm):
    email = StringField("Epost",[validators.Email()])
    firstname = StringField("Förnamn",[validators.Length(min=5, max=40)])
    lastname = StringField("Efternamn",[validators.Length(min=5, max=40)])
    
    val = []
    val.append(validators.Length(min=5, max=30))
    val.append(validators.EqualTo('pwdagain'))
    pwd = StringField("pwd",val)

    pwdagain = StringField("pwdagain",[validators.Length(min=5, max=30)])
    updates = BooleanField("Send me important updates")
