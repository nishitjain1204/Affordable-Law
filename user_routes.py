from flask import Flask, render_template,url_for,flash,redirect,session,sessions,abort,request
import os
import re
from flask_sqlalchemy import SQLAlchemy
from PIL import Image
# from sqlalchemy import exc
from models import SavedLawyers,db ,Lawyer,Lawyer_case,Lawyer_prof_qualif_1,Lawyer_prof_qualif_2,Lawyer_prof_qualif_3 , Lawyer_educational_qualif_1,Lawyer_educational_qualif_2,Lawyer_educational_qualif_3,User
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
	user_id = session['customer_id']
	saved_lawyers_ids = SavedLawyers.query.filter_by(user_id=user_id).all()
	saved_lawyers=[]
	for lawyer_id in saved_lawyers_ids:
		lawyer=Lawyer.query.filter_by(id=lawyer_id.lawyer_id).first()
		saved_lawyers.append(lawyer)

	return render_template('user_home.html',free_lawyers=free_lawyers,saved_lawyers=saved_lawyers)


@app.route('/userregister',methods=['GET','POST'])
def userregister():
	form=RegistrationForm()
	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data , method='sha256')
	
		new_user = User(username=form.username.data , email_id = form.email.data  , password = hashed_password)
		db.session.add(new_user)
		
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


@app.route("/userlogout")
@login_required
def userlogout():
    logout_user()
    return redirect(url_for('about'))



@app.route('/show_profile/<int:lawyer_id>',methods=['GET'])
@login_required
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
 

@app.route('/save/<int:lawyer_id>')
@login_required
def save_lawyer(lawyer_id):
    
	user_id = session['customer_id']
	saved_lawyer = SavedLawyers.query.filter_by(lawyer_id=lawyer_id,user_id=user_id).first()
	if saved_lawyer:
		return redirect(url_for('userhome'))
	else:
		saved_lawyer = SavedLawyers(lawyer_id=lawyer_id,user_id=user_id)
		db.session.add(saved_lawyer)
		db.session.commit()

	
	return redirect(url_for('userhome'))


@app.route('/savedlawyers')
@login_required
def savedlawyers():
	free_lawyers = Lawyer.query.filter_by(open_for_cases=1).all()
	user_id = session['customer_id']
	saved_lawyers_ids = SavedLawyers.query.filter_by(user_id=user_id).all()
	saved_lawyers=[]
	for lawyer_id in saved_lawyers_ids:
		lawyer=Lawyer.query.filter_by(id=lawyer_id.lawyer_id).first()
		saved_lawyers.append(lawyer)

	return render_template('show_saved_lawyers.html',saved_lawyers=saved_lawyers,free_lawyers=free_lawyers)


@app.route('/unsave/<int:lawyer_id>',methods = ['GET','POST'])
@login_required
def unsave_lawyer(lawyer_id):
	user_id = session['customer_id']
	saved_lawyers_list = SavedLawyers.query.filter_by(user_id=user_id).all()
	saved_lawyer = SavedLawyers.query.filter_by(user_id=user_id,lawyer_id=lawyer_id).first()
	if saved_lawyer:
		db.session.delete(saved_lawyer)
		db.session.commit()
	return redirect(url_for('userhome'))