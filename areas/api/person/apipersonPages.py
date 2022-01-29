from flask import Blueprint, render_template, request, url_for, redirect
from models import Person, db
from flask import jsonify


apiPersonBluePrint =  Blueprint('apipersoner', __name__)

class PersonApiModel:
    id = 0
    namn = ""
    city = ""
    postalcode = ""
    position = ""


def _mapPersonToApi(person):
    personApiModel = PersonApiModel()
    personApiModel.id = person.id
    personApiModel.namn = person.namn
    personApiModel.city = person.city
    personApiModel.postalcode = person.postalcode
    if person.position == "g":
        personApiModel.position = "Goalie"
    elif person.position == "d":
        personApiModel.position = "Defence"
    elif person.position == "f":
        personApiModel.position = "Forward"
    return personApiModel

def _mapJsonToPerson(data,person):
    person.namn = data["namn"]
    person.namn = data["namn"]
    person.city = data["city"]
    person.postalcode = data["postalcode"]
    if data["position"] == "Goalie":
        person.position = "Goalie"
    if data["position"] == "Defence":
        person.position = "Defence"
    if data["position"] == "Forward":
        person.position = "Forward"
    return person

@apiPersonBluePrint.route('/api/person', methods=["GET"])
def allaPersoner():
    listaMedPersoner = []
    for person in Person.query.all():
        personApiModel = _mapPersonToApi(person)
        listaMedPersoner.append(personApiModel)
    return jsonify([apiPerson.__dict__ for apiPerson in listaMedPersoner])

@apiPersonBluePrint.route('/api/person/<id>', methods=["GET"])
def getOne(id):
    person = Person.query.filter(Person.id == id).first()
    personApiModel = _mapPersonToApi(person)
    return jsonify(personApiModel.__dict__)


@apiPersonBluePrint.route('/api/person', methods=["POST"])
def create():
    data = request.get_json()
    id = int(data["id"])
    person = Person.query.filter(Person.id == id).first()
    person = _mapJsonToPerson(data, person)
    db.session.commit()
    return ''

@apiPersonBluePrint.route('/api/person/<id>', methods=["PUT"])
def update( id):
    data = request.get_json()
    id = int(data["id"])
    person = Person()
    person = _mapJsonToPerson(data, person)
    db.session.commit()
    return ''
