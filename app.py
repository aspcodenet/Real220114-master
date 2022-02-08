from flask import Flask, render_template, request, url_for, redirect
from models import db, Person, seedData,UserRegistration
from syncSearchEngine import createIndex, addDocuments
from flask_migrate import Migrate, upgrade

from areas.site.sitePages import siteBluePrint
from areas.personer.personerPages import personerBluePrint
from areas.userregistration.userRegistrationPages import userRegistrationBluePrint
from areas.api.person.apipersonPages import apiPersonBluePrint
from areas.company.companyPages import companyBluePrint

app = Flask(__name__)
app.config.from_object('config.ConfigDebug')

db.app = app
db.init_app(app)
migrate = Migrate(app,db)

app.register_blueprint(siteBluePrint)
app.register_blueprint(personerBluePrint)
app.register_blueprint(userRegistrationBluePrint)
app.register_blueprint(apiPersonBluePrint)
app.register_blueprint(companyBluePrint)







if __name__  == "__main__":
    with app.app_context():
        upgrade()
        seedData()
        createIndex()
        addDocuments()
    app.run()


