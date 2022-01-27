from flask import Flask, render_template, request, url_for, redirect
from models import db, Person, seedData,UserRegistration
from flask_migrate import Migrate, upgrade

from areas.site.sitePages import siteBluePrint
from areas.personer.personerPages import personerBluePrint
from areas.userregistration.userRegistrationPages import userRegistrationBluePrint

app = Flask(__name__)
app.config.from_object('config.ConfigDebug')

db.app = app
db.init_app(app)
migrate = Migrate(app,db)

app.register_blueprint(siteBluePrint)
app.register_blueprint(personerBluePrint)
app.register_blueprint(userRegistrationBluePrint)







if __name__  == "__main__":
    with app.app_context():
        upgrade()
        seedData()
    app.run()


