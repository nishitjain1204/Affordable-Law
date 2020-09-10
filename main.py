from flask import Flask, render_template,url_for,flash,redirect
import os
<<<<<<< HEAD
<<<<<<< HEAD:flaskblog.py
=======
<<<<<<<< HEAD:main.py
from forms import RegistrationForm,LoginForm,ProfileForm
from flask_sqlalchemy import SQLAlchemy
from models import db ,Lawyer
from  werkzeug.security import generate_password_hash , check_password_hash
from flask_login import LoginManager , UserMixin , login_user , logout_user , login_required , current_user
app = Flask(__name__) 
========
>>>>>>> c5ca5fdc5e8665c928783ee6114c8ee83de98a2f
from forms import RegistrationForm,LoginForm,ProfileForm,CaseForm
app = Flask(__name__) # so that flask knows where to look for your templates and static foles
#we made an 'app' variable and set it to  an instance of the flask class
#decorators are used to add functionality to ur already existing functions
#routes are what we typw into our browser to go to diffwrent pages 
#the route decorator shows us what would be shown on our website for that specific route

#posts is a list of dictionaries
#each dictionary represents a blog post
<<<<<<< HEAD
=======
from forms import RegistrationForm,LoginForm,ProfileForm
from flask_sqlalchemy import SQLAlchemy
from models import db ,Lawyer
from  werkzeug.security import generate_password_hash , check_password_hash
from flask_login import LoginManager , UserMixin , login_user , logout_user , login_required , current_user
app = Flask(__name__) 
>>>>>>> c5ca5fdc5e8665c928783ee6114c8ee83de98a2f:main.py
=======
>>>>>>>> c5ca5fdc5e8665c928783ee6114c8ee83de98a2f:flaskblog.py
>>>>>>> c5ca5fdc5e8665c928783ee6114c8ee83de98a2f

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models.sqlite3' 
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


@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html',posts=post) #whatever vairable 'here posts' we 
    #pass into the braces.. we will have access to it in our templates
    # you could do return '''<!doctype html>
    #<html code here>'''

@app.route('/about')
def about():
    return render_template('about.html',title='hola')


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
def cases():
	form=CaseForm()
	if form.validate_on_submit():
		flash(f'Case added for {form.Name.data}','success')
		return redirect(url_for('home'))
	return render_template('case.html',title='case',form=form)



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