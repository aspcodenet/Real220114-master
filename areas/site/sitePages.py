from flask import Blueprint, render_template
from models import Person

siteBluePrint =  Blueprint('sitePages', __name__,
                        template_folder='/templates/site')


@siteBluePrint.route("/")
def indexPage():
    activePage = "startPage"
    allaPersoner = Person.query.all()
    return render_template('site/startPage.html', antalPersoner=12, totSaldo=999,activePage=activePage)

@siteBluePrint.route("/hej")
def hejPage():
    # på riktigt kolla om inloggad osv sov
    lista = ["Stefan", "Oliver", "Josefine"]
    return render_template('site/hej.html', inloggad=True, lista=lista,age=49, name="Stefan")


