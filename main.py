from flask import Flask, render_template,url_for,flash,redirect,session,sessions,abort,request
import os
import re
from flask_sqlalchemy import SQLAlchemy
from PIL import Image
# from sqlalchemy import exc
from models import db ,Lawyer,Lawyer_case,Lawyer_prof_qualif_1,Lawyer_prof_qualif_2,Lawyer_prof_qualif_3 , Lawyer_educational_qualif_1,Lawyer_educational_qualif_2,Lawyer_educational_qualif_3
from  werkzeug.security import generate_password_hash , check_password_hash
from flask_login import LoginManager , UserMixin , login_user , logout_user , login_required , current_user
from flask_login import login_user, current_user, logout_user, login_required
from forms import RegistrationForm,LoginForm,ProfileForm,CaseForm
from werkzeug.utils import secure_filename
app = Flask(__name__) 

# so that flask knows where to look for your templates and static foles
#we made an 'app' variable and set it to  an instance of the flask class
#decorators are used to add functionality to ur already existing functions
#routes are what we typw into our browser to go to diffwrent pages 
#the route decorator shows us what would be shown on our website for that specific route

# def image_cropper(image_file):
# 	filename = image_file.filename
# 	image = Image.open(image_file)
# 	img = image.resize((668,690))
# 	img.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
# 	return img
	

# required_dimesions = (668,690)
#posts is a list of dictionaries
#each dictionary represents a blog post

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models.sqlite3' 
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif','.pdf','.txt','.doc','.docx','.jpeg']
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


from lawyer_routes import *

if __name__=='__main__':
	db.create_all(app=app)
	app.run(debug=True)

#template inheritance so that we dont have to repeaat code again and again
#a block is the part which the child overrides
#new function called url_for it will find the exact location for routes for us
#the hidden_tag() and key helps with preventing attacks