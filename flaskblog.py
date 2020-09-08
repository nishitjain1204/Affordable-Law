from flask import Flask, render_template,url_for,flash,redirect
import os
from forms import RegistrationForm,LoginForm,ProfileForm
app = Flask(__name__) # so that flask knows where to look for your templates and static foles
#we made an 'app' variable and set it to  an instance of the flask class
#decorators are used to add functionality to ur already existing functions
#routes are what we typw into our browser to go to diffwrent pages 
#the route decorator shows us what would be shown on our website for that specific route

#posts is a list of dictionaries
#each dictionary represents a blog post

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

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
		flash(f'Account created for {form.username.data}','success')
		return redirect(url_for('home'))
	return render_template('Registrationform.html',title='register',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'shlokaprincess101@gmail.com' and form.password.data == 'zaq1xsw2':
			flash(f' {form.email.data} has logged in','success')
			return redirect(url_for('home'))
		else:
			flash('unsucessful login, please check email and password','danger')
	
	return render_template('login.html',title='login',form=form)

@app.route('/profile',methods=['GET','POST'])
def profile():
	form=ProfileForm()
	if form.validate_on_submit():
		flash(f'Profile created for {form.FirstName.data}','success')
		return redirect(url_for('home'))
	return render_template('profile.html',title='login',form=form)



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
	app.run(debug=True)


#template inheritance so that we dont have to repeaat code again and again
#a block is the part which the child overrides
#new function called url_for it will find the exact location for routes for us
#the hidden_tag() and key helps with preventing attacks