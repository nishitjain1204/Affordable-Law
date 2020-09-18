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



SECRET_KEY = 'theSecretKey'
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models.sqlite3' 
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif','.pdf','.txt','.doc','.docx','.jpeg']
app.config['WHOOSH_BASE'] = 'whoosh'
db.init_app(app)










from lawyer_routes import *
from user_routes import *

if __name__=='__main__':
    
	db.create_all(app=app)
	app.run()
	



