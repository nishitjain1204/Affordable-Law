from flask import Flask, render_template,url_for,flash,redirect,session,sessions,abort,request
import os
import re
from flask_sqlalchemy import SQLAlchemy
from PIL import Image
from sqlalchemy import exc
from models import db ,Lawyer,Lawyer_case,Lawyer_prof_qualif_1,Lawyer_prof_qualif_2,Lawyer_prof_qualif_3 , Lawyer_educational_qualif_1,Lawyer_educational_qualif_2,Lawyer_educational_qualif_3
from  werkzeug.security import generate_password_hash , check_password_hash
from flask_login import LoginManager , UserMixin , login_user , logout_user , login_required , current_user
from flask_login import login_user, current_user, logout_user, login_required
from forms import RegistrationForm,LoginForm,ProfileForm,CaseForm,SearchForm
from werkzeug.utils import secure_filename
from main import app

lawyer_login_manager = LoginManager()
lawyer_login_manager.init_app(app)
lawyer_login_manager.login_view = 'login'

@lawyer_login_manager.user_loader
def load_lawyer(lawyer_id):
	return Lawyer.query.get(int(lawyer_id))

@app.route('/about')
@app.route('/',methods=['GET','POST'])
def about():
    return render_template('about.html') #whatever vairable 'here posts' we 
    #pass into the braces.. we will have access to it in our templates
    # you could do return '''<!doctype html>
    #<html code here>'''

@app.route('/home/',methods=['GET','POST'])
@login_required
def home():
	user_cases = Lawyer_case.query.filter_by(lawyer_id=session['user_id'])
	searchform = SearchForm()
	if searchform.validate_on_submit():
		return redirect(url_for('casesearch',query=searchform.searchinput.data))
    
	return render_template('home.html',title='HOME',user_cases=user_cases,searchform=searchform)


@app.route('/register/',methods=['GET','POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form=RegistrationForm()
	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data , method='sha256')
		existing_lawyers = Lawyer.query.all()
		if existing_lawyers:
			for lawyer in existing_lawyers:
				if form.email.data == lawyer.email_id :
					flash('Email already taken . Please try again .','danger')
					return redirect(url_for('register'))
				elif form.username.data == lawyer.username :
					flash('Username already taken. Please try again .','danger')
					return redirect(url_for('register'))

    			
		
		new_user = Lawyer(username=form.username.data , email_id = form.email.data  , password = hashed_password)
		db.session.add(new_user)
		
		
		db.session.commit()
		flash('Registration Successfull','success')
		return redirect(url_for('login'))
	return render_template('Registrationform.html',title='register',form=form)

@app.route('/login/',methods=['GET','POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		user = Lawyer.query.filter_by(email_id=form.email.data).first()
		if user :
			if check_password_hash(user.password,form.password.data):
					login_user(user,remember = form.remember.data)
					session['user_id'] = user.id
					flash(f'Login successfull','success')
					return redirect(url_for('home'))
			else:
    				flash('User Authentication Failed','danger')
		
		else:
    			flash('User Not Found','danger')
    			
						

	
	return render_template('login.html',title='login',form=form)

@app.route('/profile_update/<int:lawyer_id>',methods=['GET','POST'])
@login_required
def profile(lawyer_id):
	lawyer=Lawyer.query.filter_by(id=lawyer_id).first()
	existing_lawyers = Lawyer.query.all()
	form = ProfileForm()
	if form.validate_on_submit():
    	
		for the_lawyer in existing_lawyers:
			if the_lawyer.phone_number == form.Number.data and the_lawyer.id != lawyer_id :
				return redirect(url_for('profile',lawyer_id=session['user_id']))
		
		lawyer.first_name = form.FirstName.data
		lawyer.last_name = form.LastName.data
		
		lawyer.current_job = form.CurrentJob.data
		lawyer.open_for_cases=form.Notworking.data
		lawyer.city =  form.location.data
		lawyer.specialization1 = form.FirstSpec.data
		lawyer.specialization2 =form.SecSpec.data
		lawyer.specialization3 = form.ThirdSpec.data
		lawyer.bio = form.Bio.data
		lawyer.linkedin =   form.Linkedin.data
		lawyer.facebook = form.Facebook.data
		lawyer.instagram =  form.Instagram.data
		lawyer.min_fee= form.MinFee.data
		lawyer.max_fee= form.MaxFee.data
		lawyer.phone_number = form.Number.data
		profile_photo = form.Profilephoto.data
		
		print(type(profile_photo))

		if profile_photo:
			profile_photo_name = secure_filename(profile_photo.filename)
			if profile_photo_name != '':
				file_ext = os.path.splitext(profile_photo_name)[1]
				if file_ext not in app.config['UPLOAD_EXTENSIONS']:
					abort(400)
				profile_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], profile_photo_name))
				lawyer.profile_photo = url_for('static',filename='uploads/'+profile_photo_name)
		
		
		educational_qualif_1 = Lawyer_educational_qualif_1(educational_qualif=form.Educational_qualif_1.data, educational_institute=form.Educational_Institution_1.data,from_=form.From_1.data,to_=form.To_1.data,lawyer=lawyer)
		db.session.add(educational_qualif_1)
		educational_qualif_2 = Lawyer_educational_qualif_2(educational_qualif=form.Educational_qualif_2.data,from_=form.From_2.data,to_=form.To_2.data,lawyer=lawyer, educational_institute=form.Educational_Institution_2.data)
		db.session.add(educational_qualif_2)
		educational_qualif_3 = Lawyer_educational_qualif_3(educational_qualif=form.Educational_qualif_3.data,from_=form.From_3.data,to_=form.To_3.data,lawyer=lawyer, educational_institute = form.Educational_Institution_3.data)
		db.session.add(educational_qualif_3)
		proffesional_qualif_1 = Lawyer_prof_qualif_1(prof_qualif=form.Prof_qualif_1.data,from_prof=form.From_1.data,to_prof=form.To_1.data,lawyer=lawyer,prof_institute=form.Institution_1.data)
		db.session.add(proffesional_qualif_1)
		proffesional_qualif_2 = Lawyer_prof_qualif_2(prof_qualif=form.Prof_qualif_2.data,from_prof=form.From_2.data,to_prof=form.To_2.data,lawyer=lawyer,prof_institute=form.Institution_2.data)
		db.session.add(proffesional_qualif_2)
		proffesional_qualif_3 = Lawyer_prof_qualif_3(prof_qualif=form.Prof_qualif_3.data,from_prof=form.From_3.data,to_prof=form.To_3.data,lawyer=lawyer,prof_institute=form.Institution_3.data)
		db.session.add(proffesional_qualif_3)
		db.session.commit()
		flash(f'Profile updated for {form.FirstName.data}','success')
		return redirect(url_for('profile_display',lawyer_id=lawyer.id))

	elif request.method == 'GET':

		form.FirstName.data=lawyer.first_name 
		form.LastName.data = lawyer.last_name
		
		form.CurrentJob.data=lawyer.current_job 
		form.Notworking.data=lawyer.open_for_cases
		form.location.data=lawyer.city 
		form.FirstSpec.data=lawyer.specialization1 
		form.SecSpec.data=lawyer.specialization2 
		form.ThirdSpec.data=lawyer.specialization3  
		form.Bio.data=lawyer.bio 
		form.Linkedin.data  =    lawyer.linkedin
		form.Facebook.data = lawyer.facebook
		form.Instagram.data=lawyer.instagram 
		form.MinFee.data= lawyer.min_fee
		form.MaxFee.data = lawyer.max_fee
		form.Number.data =  lawyer.phone_number 

		edu_qualif_1=Lawyer_educational_qualif_1.query.filter_by(lawyer_id=lawyer.id).first()
		print('edu_qualif_1: ', edu_qualif_1)
		edu_qualif_2=Lawyer_educational_qualif_2.query.filter_by(lawyer_id=lawyer.id).first()
		edu_qualif_3=Lawyer_educational_qualif_3.query.filter_by(lawyer_id=lawyer.id).first()

		prof_qualif_1 = Lawyer_prof_qualif_1.query.filter_by(lawyer_id=lawyer.id).first()
		prof_qualif_2 = Lawyer_prof_qualif_2.query.filter_by(lawyer_id=lawyer.id).first()
		prof_qualif_3 = Lawyer_prof_qualif_3.query.filter_by(lawyer_id=lawyer.id).first()

		if edu_qualif_1:
			form.Educational_qualif_1.data = edu_qualif_1.educational_qualif
			form.From_1.data = edu_qualif_1.from_
			form.To_1.data = edu_qualif_1.to_
			form.Educational_Institution_1.data = edu_qualif_1.educational_institute
		
		if edu_qualif_2:
			form.Educational_qualif_2.data = edu_qualif_2.educational_qualif
			form.Educational_Institution_2.data = edu_qualif_2.educational_institute
			form.From_2.data = edu_qualif_2.from_
			form.To_2.data = edu_qualif_2.to_
		
		if edu_qualif_3 :
			form.Educational_qualif_3.data = edu_qualif_3.educational_qualif
			form.From_3.data = edu_qualif_3.from_
			form.To_3.data = edu_qualif_3.to_
			form.Educational_Institution_3.data = edu_qualif_3.educational_institute
		
		if prof_qualif_1:
			form.Prof_qualif_1.data = prof_qualif_1.prof_qualif
			form.From_prof_1.data = prof_qualif_1.from_prof
			form.To_prof_1.data = prof_qualif_1.to_prof
			form.Institution_1.data = prof_qualif_1.prof_institute
		

		if prof_qualif_2:
    			
			form.Prof_qualif_2.data = prof_qualif_2.prof_qualif
			form.From_prof_2.data = prof_qualif_2.from_prof
			form.To_prof_2.data = prof_qualif_2.to_prof
			form.Institution_2.data = prof_qualif_2.prof_institute
		
		if prof_qualif_3 :

			form.Prof_qualif_3.data = prof_qualif_3.prof_qualif
			form.From_prof_3.data = prof_qualif_3.from_prof
			form.To_prof_3.data = prof_qualif_3.to_prof
			form.Institution_3.data = prof_qualif_3.prof_institute
		
		

		
		
    	
    	
		
	return render_template('profile.html',title='login',form=form)


@app.route('/profile_display/<int:lawyer_id>',methods=['GET','POST'])
def profile_display(lawyer_id):
	lawyer=Lawyer.query.filter_by(id=lawyer_id).first()
	edu_qualif_1=Lawyer_educational_qualif_1.query.filter_by(lawyer_id=lawyer.id).first()
	print('edu_qualif_1: ', edu_qualif_1)
	edu_qualif_2=Lawyer_educational_qualif_2.query.filter_by(lawyer_id=lawyer.id).first()
	edu_qualif_3=Lawyer_educational_qualif_3.query.filter_by(lawyer_id=lawyer.id).first()

	prof_qualif_1 = Lawyer_prof_qualif_1.query.filter_by(lawyer_id=lawyer.id).first()
	prof_qualif_2 = Lawyer_prof_qualif_2.query.filter_by(lawyer_id=lawyer.id).first()
	prof_qualif_3 = Lawyer_prof_qualif_3.query.filter_by(lawyer_id=lawyer.id).first()
	return render_template ('profile_display.html',lawyer=lawyer,edu_qualif_1=edu_qualif_1,edu_qualif_2=edu_qualif_2,edu_qualif_3=edu_qualif_3,prof_qualif_1 = prof_qualif_1,prof_qualif_2 =prof_qualif_2,prof_qualif_3 =prof_qualif_3)
 

@app.route('/cases/',methods=['GET','POST'])
@login_required
def cases():
	form=CaseForm()

	if form.validate_on_submit():
		name = form.Name.data
		day = form.Day.data
		month = form.Month.data
		year = form.Year.data
		bio = form.Bio.data
		lawyer_id = session['user_id']
		case=Lawyer_case(name=name,day=day,month=month,year=year,lawyer_id=lawyer_id,bio=bio)
		case_file = form.case_file.data
		if case_file:
			case_file_name = secure_filename(case_file.filename)
			if case_file_name != '':
				file_ext = os.path.splitext(case_file_name)[1]
				if file_ext not in app.config['UPLOAD_EXTENSIONS']:
					abort(400)
				case_file.save(os.path.join(app.config['UPLOAD_FOLDER'], case_file_name))
				case.case_file = url_for('static',filename='uploads/'+case_file_name)
		else:
			case.case_file = None
		
		
		
		db.session.add(case)
		db.session.commit()

		flash(f'Case added for {form.Name.data}','success')
		return redirect(url_for('home'))
	return render_template('case.html',title='case',form=form , legend='NEW CASE')
	

@app.route('/case_display/<int:case_id>',methods=['GET','POST'])
def case_display(case_id):
	searchform = SearchForm()
	if searchform.validate_on_submit():
		return redirect(url_for('casesearch',query=searchform.searchinput.data))
	case=Lawyer_case.query.get_or_404(case_id)
	return render_template('case_display.html',case=case,searchform=searchform)

@app.route('/case_display/<int:case_id>/update', methods = ['GET','POST'])
@login_required
def case_update(case_id):
	# searchform = SearchForm()
	# if searchform.validate_on_submit():
	# 	return redirect(url_for('casesearch',query=searchform.searchinput.data))

	case=Lawyer_case.query.get_or_404(case_id)
	if case.lawyer_id != session['user_id']:
		abort(403)
	form=CaseForm()
	
	
	# form.case_file.data = open(os.path.join(app.config['UPLOAD_FOLDER'],filename[1]),'r+')
	if form.validate_on_submit():
		case.name = form.Name.data
		case.day = form.Day.data
		case.month = form.Month.data
		case.year = form.Year.data
		case.bio = form.Bio.data
		case_file = form.case_file.data
		print(case_file)
		if case_file:
			case_file_name = secure_filename(case_file.filename)
			if case_file_name != '':
				file_ext = os.path.splitext(case_file_name)[1]
				if file_ext not in app.config['UPLOAD_EXTENSIONS']:
					abort(400)
				case_file.save(os.path.join(app.config['UPLOAD_FOLDER'], case_file_name))
				case.case_file = url_for('static',filename='uploads/'+case_file_name)

		db.session.commit()
		flash('Case Updated','success')
		return redirect(url_for('home'))

	elif request.method == 'GET':
    	
		form.Name.data = case.name
		form.Day.data = case.day
		form.Month.data = case.month
		form.Year.data = case.year
		form.Bio.data = case.bio
    	
		
		
	return render_template('case.html',title='UPDATE CASE',form=form,legend='UPDATE CASE',warning='this will overwrite the previously uploaded file')

@app.route('/case_display/<int:case_id>/delete/', methods = ['POST'])
@login_required
def delete_case(case_id):
	case=Lawyer_case.query.get_or_404(case_id)
	if case.lawyer_id != session['user_id']:
		abort(403)
	db.session.delete(case)
	db.session.commit()
	flash('Your case has been deleted ','success')
	return redirect(url_for('home'))

@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for('about'))





@app.route('/casesearch/<query>',methods=['GET','POST'])
@login_required
def casesearch(query):
	searchform = SearchForm()
	if searchform.validate_on_submit():
		return redirect(url_for('casesearch',query=searchform.searchinput.data))
	

	user_cases = Lawyer_case.query.filter_by(lawyer_id=session['user_id'])
	print(query)

	searched_cases= []
	for case in user_cases :
		if query in case.name:
			searched_cases.append(case)
		elif query in case.day :
			searched_cases.append(case)
		elif query in case.month :
			searched_cases.append(case)
		elif query in case.year:
			searched_cases.append(case)
		elif query in case.bio :
			searched_cases.append(case)
		
			
    		

	return render_template('show_searched_cases.html',searched_cases=searched_cases,searchform=searchform)

