from flask import Blueprint, render_template
from models import Person
from areas.userregistration.forms import UserRegistrationForm

userRegistrationBluePrint =  Blueprint('userRegistrationPages', __name__,
                        template_folder='/templates/userRegistration')



@userRegistrationBluePrint.route("/userconfirmation")
def userConfirmationPage():
    namnet = request.args.get('namn',"")
    return render_template('userconfirmation.html',namn=namnet)

@userRegistrationBluePrint.route("/newuser",methods=["GET", "POST"]) 
def userRegistrationPage():
    form = UserRegistrationForm(request.form) 
    if request.method == "GET":
        return render_template('userregistration.html',form=form)
    if form.validate_on_submit():
        userReg = UserRegistration()
        userReg.email = form.email.data
        userReg.firstname = form.firstname.data
        userReg.lastname = form.lastname.data
        userReg.password = form.pwd.data
        userReg.updates = form.updates.data
        db.session.add(userReg)
        db.session.commit()
        return redirect(url_for('userConfirmationPage', namn=form.firstname.data ))

    return render_template('userregistration.html',form=form)

