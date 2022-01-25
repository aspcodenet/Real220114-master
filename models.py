from flask_sqlalchemy import SQLAlchemy
import barnum

db = SQLAlchemy()


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(80), unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    postalcode = db.Column(db.String(10), unique=False, nullable=False)
    position = db.Column(db.String(1), unique=False, nullable=False) # G, D, F

class UserRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=False, nullable=False)
    firstname = db.Column(db.String(40), unique=False, nullable=False)
    lastname = db.Column(db.String(40), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    updates = db.Column(db.Boolean, unique=False, nullable=False)  



def seedData():
    antal =  Person.query.count()
    while antal < 100:
        person = Person()
        person.postalcode, person.city, _  = barnum.create_city_state_zip()
        namn1, namn2 = barnum.create_name()
        person.namn = namn1 + " " + namn2
        antal = antal + 1
        db.session.add(person)
        db.session.commit()        



