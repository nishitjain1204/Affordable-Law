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
from forms import RegistrationForm,LoginForm,ProfileForm,CaseForm,SearchForm
from werkzeug.utils import secure_filename
from main import app
import flask_whooshalchemy as wa





@app.route('/userhome/',methods=['GET','POST'])

def userhome():
	searchform = SearchForm()
	if searchform.validate_on_submit():
		return redirect(url_for('lawyersearch',query=searchform.searchinput.data))
	free_lawyers = Lawyer.query.filter_by(open_for_cases=1).all()

	return render_template('user_home.html',free_lawyers=free_lawyers,searchform=searchform)





@app.route('/show_profile/<int:lawyer_id>',methods=['GET','POST'])

def show_profile(lawyer_id):
	searchform = SearchForm()
	if searchform.validate_on_submit():
		return redirect(url_for('lawyersearch',query=searchform.searchinput.data))
	lawyer=Lawyer.query.filter_by(id=lawyer_id).first()
	edu_qualif_1=Lawyer_educational_qualif_1.query.filter_by(lawyer_id=lawyer.id).first()
	print('edu_qualif_1: ', edu_qualif_1)
	edu_qualif_2=Lawyer_educational_qualif_2.query.filter_by(lawyer_id=lawyer.id).first()
	edu_qualif_3=Lawyer_educational_qualif_3.query.filter_by(lawyer_id=lawyer.id).first()

	prof_qualif_1 = Lawyer_prof_qualif_1.query.filter_by(lawyer_id=lawyer.id).first()
	prof_qualif_2 = Lawyer_prof_qualif_2.query.filter_by(lawyer_id=lawyer.id).first()
	prof_qualif_3 = Lawyer_prof_qualif_3.query.filter_by(lawyer_id=lawyer.id).first()
	return render_template ('show_lawyer_profile.html',lawyer=lawyer,edu_qualif_1=edu_qualif_1,edu_qualif_2=edu_qualif_2,edu_qualif_3=edu_qualif_3,prof_qualif_1 = prof_qualif_1,prof_qualif_2 =prof_qualif_2,prof_qualif_3 =prof_qualif_3,searchform=searchform )
 



@app.route('/lawyersearch/<query>',methods=['GET','POST'])

def lawyersearch(query):
	searchform = SearchForm()
	if searchform.validate_on_submit():
		return redirect(url_for('lawyersearch',query=searchform.searchinput.data))

	free_lawyers = Lawyer.query.filter_by(open_for_cases=1).all()
	print(query)

	searched_lawyers= []
	for lawyer in free_lawyers :
		if query in lawyer.username:
			searched_lawyers.append(lawyer)
		elif query in lawyer.first_name :
			searched_lawyers.append(lawyer)
		elif query in lawyer.last_name :
			searched_lawyers.append(lawyer)
		elif query in lawyer.email_id :
			searched_lawyers.append(lawyer)
		elif query in lawyer.current_job :
			searched_lawyers.append(lawyer)
		elif query in lawyer.city :
			searched_lawyers.append(lawyer)
		elif query in lawyer.specialization1 :
			searched_lawyers.append(lawyer)
		elif query in lawyer.specialization2:
			searched_lawyers.append(lawyer)
		elif query in lawyer.specialization3:
			searched_lawyers.append(lawyer)
			
    		

	return render_template('show_searched_lawyers.html',free_lawyers=free_lawyers,searched_lawyers=searched_lawyers,searchform=searchform)

