from flask import Flask, render_template, request
from models import db, Person, seedData
from flask_migrate import Migrate, upgrade
from random import randint
from forms import PersonEditForm

app = Flask(__name__)
app.config.from_object('config.ConfigDebug')

db.app = app
db.init_app(app)
migrate = Migrate(app,db)

@app.route("/hej")
def hejPage():
    # på riktigt kolla om inloggad osv sov
    lista = ["Stefan", "Oliver", "Josefine"]
    return render_template('hej.html', inloggad=True, lista=lista,age=49, name="Stefan")



@app.route("/")
def indexPage():
    activePage = "startPage"
    allaPersoner = Person.query.all()
    #antalPersoner = Person count???
    #totSaldo = 
    return render_template('startPage.html', antalPersoner=12, totSaldo=999,activePage=activePage)

# To improve: get med defaultvalue
# search!
@app.route("/personer")
def personerPage():
    
    sortColumn = request.args.get('sortColumn', 'namn')
    sortOrder = request.args.get('sortOrder', 'asc')
    page = int(request.args.get('page', 1))

    searchWord = request.args.get('q','')

    activePage = "personerPage"
    allaPersoner = Person.query.filter(
        Person.namn.like('%' + searchWord + '%') | 
        Person.city.like('%' + searchWord + '%')  | 
        Person.id.like(searchWord)          )

    if sortColumn == "namn":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Person.namn.desc())
        else:
            allaPersoner = allaPersoner.order_by(Person.namn.asc())

    if sortColumn == "city":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Person.city.desc())
        else:
            allaPersoner = allaPersoner.order_by(Person.city.asc())

    if sortColumn == "postal":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Person.postalcode.desc())
        else:
            allaPersoner = allaPersoner.order_by(Person.postalcode.asc())

    paginationObject = allaPersoner.paginate(page,20,False)


    return render_template('personer.html', 
            allaPersoner=paginationObject.items, 
            page=page,
            sortColumn=sortColumn,
            sortOrder=sortOrder,
            q=searchWord,
            has_next=paginationObject.has_next,
            has_prev=paginationObject.has_prev, 
            pages=paginationObject.pages, 
            activePage=activePage)

@app.route("/person/<id>")  # EDIT   3
def personPage(id):
    personFromDb = Person.query.filter(Person.id == id).first()
    form = PersonEditForm(request.form) 
    form.name.data = personFromDb.namn
    form.city.data = personFromDb.city
    form.postalcode.data = int(personFromDb.postalcode)
    return render_template('person.html',person=person, form=form)




@app.route("/hopp")
def hoppPage():
    return "<html><body><h1>Hopp</h1></body></html>"

@app.route("/personer2")
def personerPage2():
    
    sortColumn = request.args.get('sortColumn',"namn")
    sortOrder = request.args.get('sortOrder', "asc")
    page = request.args.get('page', 1, type=int)

    activePage = "personerPage"
    allaPersoner = Person.query


    if sortColumn == "namn":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Person.namn.desc())
        else:
            allaPersoner = allaPersoner.order_by(Person.namn.asc())

    if sortColumn == "city":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Person.city.desc())
        else:
            allaPersoner = allaPersoner.order_by(Person.city.asc())

    if sortColumn == "postal":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Person.postalcode.desc())
        else:
            allaPersoner = allaPersoner.order_by(Person.postalcode.asc())

    paginationObject = allaPersoner.paginate(page,20,False)

    return render_template('personer.html', 
                    allaPersoner=paginationObject.items, 
            activePage=activePage)



if __name__  == "__main__":
    with app.app_context():
        upgrade()
        seedData()
    app.run()


