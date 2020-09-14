from flask import Flask, render_template,url_for,flash,redirect,session,sessions,abort,request
import os
import re
from flask_sqlalchemy import SQLAlchemy
from PIL import Image
# from sqlalchemy import exc
from models import db ,Lawyer,Lawyer_case,Lawyer_prof_qualif_1,Lawyer_prof_qualif_2,Lawyer_prof_qualif_3 , Lawyer_educational_qualif_1,Lawyer_educational_qualif_2,Lawyer_educational_qualif_3,User
from  werkzeug.security import generate_password_hash , check_password_hash
from flask_login import LoginManager , UserMixin , login_user , logout_user , login_required , current_user
from flask_login import login_user, current_user, logout_user, login_required
from forms import RegistrationForm,LoginForm,ProfileForm,CaseForm
from werkzeug.utils import secure_filename
from main import app

user_login_manager = LoginManager()
user_login_manager.init_app(app)
user_login_manager.login_view = 'userlogin'

@user_login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))



@app.route('/userhome')
@login_required
def userhome():
    free_lawyers = Lawyer.query.filter_by(open_for_cases=1).all()
    
    return render_template('user_home.html',title='userHOME',free_lawyers=free_lawyers)


@app.route('/userregister',methods=['GET','POST'])
def userregister():
	form=RegistrationForm()
	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data , method='sha256')
		try:
			new_user = User(username=form.username.data , email_id = form.email.data  , password = hashed_password)
			db.session.add(new_user)
		except exc.SQLAlchemyError as e :
			return "<h1>{{ e }}</h1>"
		
		db.session.commit()
		flash('Registration Successfull','success')
		return redirect(url_for('userlogin'))
	return render_template('user_Registrationform.html',title='register',form=form)

@app.route('/userlogin',methods=['GET','POST'])
def userlogin():
	form=LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email_id=form.email.data).first()
		if user :
			if check_password_hash(user.password,form.password.data):
					login_user(user,remember = form.remember.data)
					session['customer_id'] = user.id
					flash(f'Login successfull','success')
					return redirect(url_for('userhome'))
			else:
    				flash('User Authentication Failed','danger')
		
		else:
    			flash('User Not Found','danger')
    			
						

	
	return render_template('userlogin.html',title='login',form=form)


@app.route("/logout")
@login_required
def userlogout():
    logout_user()
    return redirect(url_for('about'))



@app.route('/show_profile/<int:lawyer_id>',methods=['GET'])
def show_profile(lawyer_id):
	lawyer=Lawyer.query.filter_by(id=lawyer_id).first()
	edu_qualif_1=Lawyer_educational_qualif_1.query.filter_by(lawyer_id=lawyer.id).first()
	print('edu_qualif_1: ', edu_qualif_1)
	edu_qualif_2=Lawyer_educational_qualif_2.query.filter_by(lawyer_id=lawyer.id).first()
	edu_qualif_3=Lawyer_educational_qualif_3.query.filter_by(lawyer_id=lawyer.id).first()

	prof_qualif_1 = Lawyer_prof_qualif_1.query.filter_by(lawyer_id=lawyer.id).first()
	prof_qualif_2 = Lawyer_prof_qualif_2.query.filter_by(lawyer_id=lawyer.id).first()
	prof_qualif_3 = Lawyer_prof_qualif_3.query.filter_by(lawyer_id=lawyer.id).first()
	return render_template ('show_lawyer_profile.html',lawyer=lawyer,edu_qualif_1=edu_qualif_1,edu_qualif_2=edu_qualif_2,edu_qualif_3=edu_qualif_3,prof_qualif_1 = prof_qualif_1,prof_qualif_2 =prof_qualif_2,prof_qualif_3 =prof_qualif_3)
 



