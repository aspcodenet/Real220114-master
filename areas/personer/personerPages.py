from flask import Blueprint, render_template, request, url_for, redirect
from models import Person, db, CreditCard
from areas.personer.forms import PersonEditForm, PersonNewForm

personerBluePrint =  Blueprint('personer', __name__,
                        template_folder='/templates/personer')


# To improve: get med defaultvalue
# search!
@personerBluePrint.route("/personer")
def personerPage():
    
    sortColumn = request.args.get('sortColumn', 'namn')
    sortOrder = request.args.get('sortOrder', 'asc')
    page = int(request.args.get('page', 1))

    searchWord = request.args.get('q','')

    # productName  Blå stol 2022
    # searchWord - stolar, 
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


    return render_template('personer/personer.html', 
            allaPersoner=paginationObject.items, 
            page=page,
            sortColumn=sortColumn,
            sortOrder=sortOrder,
            q=searchWord,
            has_next=paginationObject.has_next,
            has_prev=paginationObject.has_prev, 
            pages=paginationObject.pages, 
            activePage=activePage)


@personerBluePrint.route("/personer/new",methods=["GET", "POST"]) 
def personNewPage():
    form = PersonNewForm(request.form) 

    if request.method == "GET":
        return render_template('personer/personnew.html',form=form)

    if form.validate_on_submit():
        personFromDb = Person()
        personFromDb.namn = form.name.data
        personFromDb.city = form.city.data 
        personFromDb.postalcode = str(form.postalcode.data)
        personFromDb.position = form.position.data
        db.session.add(personFromDb)
        db.session.commit()
        return redirect(url_for('personer.personerPage'))

    return render_template('personer/personnew.html',form=form)



@personerBluePrint.route("/personer/card/<id>",methods=["GET"])  # EDIT   3
def cardPage(id):
    personFromDb = Person.query.filter(Person.id == id).first()
    #cards = CreditCard.query.filter(CreditCard.PersonId == id).order_by(CreditCard.Datum.desc())
    cards = []
    return render_template('personer/cardPage.html',person=personFromDb, cards=cards)


@personerBluePrint.route("/personer/edit/<id>",methods=["GET", "POST"])  # EDIT   3
def personPage(id):
    form = PersonEditForm(request.form) 
    personFromDb = Person.query.filter(Person.id == id).first()

    if request.method == "GET":
        form.name.data = personFromDb.namn
        form.city.data = personFromDb.city
        form.postalcode.data = int(personFromDb.postalcode)
        form.position.data = personFromDb.position
        return render_template('personer/person.html',person=personFromDb, form=form)
    if form.validate_on_submit():
        personFromDb.namn = form.name.data
        personFromDb.city = form.city.data 
        personFromDb.position = form.position.data
        personFromDb.postalcode = str(form.postalcode.data)
        db.session.commit()
        return redirect(url_for('personerPage'))
    return render_template('personer/person.html',person=personFromDb, form=form)
    







