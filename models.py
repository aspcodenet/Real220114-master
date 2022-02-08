from flask_sqlalchemy import SQLAlchemy
import barnum
import random
import datetime

db = SQLAlchemy()


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(80), unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    postalcode = db.Column(db.String(10), unique=False, nullable=False)
    position = db.Column(db.String(1), unique=False, nullable=False) # G, D, F
    cards = db.relationship('CreditCard', backref='Person',lazy=True)


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(80), unique=False, nullable=False)
    street = db.Column(db.String(80), unique=False, nullable=False)
    postalcode = db.Column(db.String(10), unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    phone = db.Column(db.String(20), unique=False, nullable=False)



class CreditCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardtype = db.Column(db.String(30), unique=False, nullable=False)
    number = db.Column(db.String(30), unique=False, nullable=False)
    PersonId = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    Datum = db.Column(db.DateTime, unique=False, nullable=False)


class UserRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=False, nullable=False)
    firstname = db.Column(db.String(40), unique=False, nullable=False)
    lastname = db.Column(db.String(40), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    updates = db.Column(db.Boolean, unique=False, nullable=False)  



def seedData():
    antal =  Company.query.count()
    while antal < 100:
        company = Company()
        company.postalcode, company.city, _  = barnum.create_city_state_zip()
        namn1, namn2 = barnum.create_name()
        company.namn = barnum.create_company_name()
        company.phone = barnum.create_phone()
        company.street = barnum.create_nouns() + " St"
        antal = antal + 1
        db.session.add(company)
        db.session.commit()     


    antal =  Person.query.count()
    while antal < 100:
        person = Person()
        person.postalcode, person.city, _  = barnum.create_city_state_zip()
        namn1, namn2 = barnum.create_name()
        person.namn = namn1 + " " + namn2
        antal = antal + 1
        db.session.add(person)
        db.session.commit()     
    antal =  CreditCard.query.count()   
    if antal > 100:
        return
    for person in Person.query.all():
        for x in range(3,random.randint(3, 30)):
            namn,number = barnum.create_cc_number()
            c = CreditCard()
            c.cardtype = namn
            c.number = number[0]
            c.Datum = barnum.create_date(past=True)
            person.cards.append(c)
        db.session.commit()




