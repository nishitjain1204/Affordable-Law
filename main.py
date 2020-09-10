from flask import Flask, render_template,url_for,flash,redirect,session,sessions,abort
import os
from flask_sqlalchemy import SQLAlchemy
from models import db ,Lawyer,Lawyer_case
from  werkzeug.security import generate_password_hash , check_password_hash
from flask_login import LoginManager , UserMixin , login_user , logout_user , login_required , current_user
from forms import RegistrationForm,LoginForm,ProfileForm,CaseForm
from werkzeug.utils import secure_filename
app = Flask(__name__) # so that flask knows where to look for your templates and static foles
#we made an 'app' variable and set it to  an instance of the flask class
#decorators are used to add functionality to ur already existing functions
#routes are what we typw into our browser to go to diffwrent pages 
#the route decorator shows us what would be shown on our website for that specific route

#posts is a list of dictionaries
#each dictionary represents a blog post

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models.sqlite3' 
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif','.pdf','.txt','.doc','.docx']
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_lawyer(lawyer_id):
	return Lawyer.query.get(int(lawyer_id))


post =[
{
	'author':"corey",
	'title':"hey",
	'content':"pata nahi yaar",
	'date':'20 april'
},
{
	'author':"coy",
	'title':"he",
	'content':"pata yaar",
	'date':'20 may'
}

]

# <!--codeblock is rep by {% %} -->
#<!-- {{}} is used to put up a variabke-->
#<!--codeblock is used again to show end of the for loop by {% %} -->


@app.route('/about')
@app.route('/')
def about():
    return render_template('about.html',posts=post) #whatever vairable 'here posts' we 
    #pass into the braces.. we will have access to it in our templates
    # you could do return '''<!doctype html>
    #<html code here>'''

@app.route('/home')
def home():
    user_cases = Lawyer_case.query.filter_by(lawyer_id=session['user_id'])
    return render_template('home.html',title='HOME',user_cases=user_cases)


@app.route('/register',methods=['GET','POST'])
def register():
	form=RegistrationForm()
	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data , method='sha256')
		new_user = Lawyer(username=form.username.data , email_id = form.email.data  , password = hashed_password)
		db.session.add(new_user)
		db.session.commit()
		flash('Registation Successfully')
	return render_template('Registrationform.html',title='register',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		user = Lawyer.query.filter_by(email_id=form.email.data).first()
		if user :
			if check_password_hash(user.password,form.password.data):
				login_user(user,remember = form.remember.data)
				session['user_id'] = user.id
				flash(f'Login successfull')
				return render_template('layout.html')
						

	
	return render_template('login.html',title='login',form=form)

@app.route('/profile',methods=['GET','POST'])
def profile():
	form=ProfileForm()
	if form.validate_on_submit():
		flash(f'Profile created for {form.FirstName.data}','success')
		return redirect(url_for('home'))
	return render_template('profile.html',title='login',form=form)

 
# @app.route('/dashboard')
# @login_required
# def dashboard():
#     return render_template('/Enterpage/Enterpage.html')

@app.route('/cases',methods=['GET','POST'])
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
	return render_template('case.html',title='case',form=form)
	

@app.route('/case_display/<int:case_id>')
def case_display(case_id):
	case=Lawyer_case.query.get_or_404(case_id)
	return render_template('case_display.html',case=case)


#@app.route('/profile')
#def profile():
#	form=ProfileForm()
#		if form.validate_on_submit():
#			flash(f'Profile created for {form.FirstName.data}','success')
#			return redirect(url_for('home'))
#	return render_template('profile.html',title='profile',form=form)



 #while setting environment variable whatever you type 
 #at like app=Flask(__name__) .. then FLASK_APP
 # if its a=Flask(__name__) .. then FLASK_A

if __name__=='__main__':
	db.create_all(app=app)
	app.run(debug=True)

#template inheritance so that we dont have to repeaat code again and again
#a block is the part which the child overrides
#new function called url_for it will find the exact location for routes for us
#the hidden_tag() and key helps with preventing attacks