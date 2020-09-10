
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import UserMixin

# from main import app 
db = SQLAlchemy()



class User(UserMixin, db.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here

    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(50), nullable = False)
    first_name = db.Column(db.String(50), nullable = False)
    middle_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    age = db.Column(db.Integer , nullable = False)
    email_id  = db.Column(db.String(200), nullable = False , unique = True)
    address = db.Column(db.String(200), nullable = False)
    city =  db.Column(db.String(50), nullable = False)
    profile_photo = db.Column(db.Integer,db.ForeignKey('user_profile_pictures.id'))
    password =  db.Column(db.String(50), nullable = False)


class Lawyer(UserMixin,db.Model):

    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(50), nullable = False)
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50) )
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer )
    email_id  = db.Column(db.String(200), nullable = False, unique = True)
    address = db.Column(db.String(200))
    city =  db.Column(db.String(50))
    educational_qualification = db.Column(db.String(100))
    specialization1 = db.Column(db.String(50))
    specialization2 = db.Column(db.String(50))
    specialization3 = db.Column(db.String(50))
    summary = db.Column(db.String(200))
    linkedin =   db.Column(db.String(200), unique = True)
    facebook =  db.Column(db.String(200), unique = True)
    instagram =  db.Column(db.String(200), unique = True)
    profile_photo = db.Column(db.Integer,db.ForeignKey('lawyer_profile_pictures.id'))
    password =  db.Column(db.String(50), nullable = False)
    cases  = db.relationship('Lawyer_case', backref = 'lawyer')

class User_profile_pictures(db.Model):

    id = db.Column(db.Integer , primary_key = True)
    image = db.Column(db.String(200))

class Lawyer_profile_pictures(db.Model):
    
    id = db.Column(db.Integer , primary_key = True)
    image = db.Column(db.String(200))

class Lawyer_case(db.Model):
    # address,telephone and faxnumbers,emailaddress, the names of opposing parties  , and key dates , conflict-searches
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(200), unique = True)
    day = db.Column(db.String(2))
    month = db.Column(db.String(2))
    year = db.Column(db.String(10))
    bio = db.Column(db.String(2000))
    case_file = db.Column(db.String(200), unique = True)
    lawyer_id = db.Column(db.Integer , db.ForeignKey('lawyer.id')) 





    






    




