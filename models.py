
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
    # first_name = db.Column(db.String(50), nullable = False)
    # middle_name = db.Column(db.String(50), nullable = False)
    # last_name = db.Column(db.String(50), nullable = False)
    # age = db.Column(db.Integer , nullable = False)
    email_id  = db.Column(db.String(200), nullable = False, unique = True)
    # address = db.Column(db.String(200), nullable = False)
    # city =  db.Column(db.String(50), nullable = False)
    # educational_qualification = db.Column(db.String(100))
    # specialization1 = db.Column(db.String(50), nullable = False)
    # specialization2 = db.Column(db.String(50), nullable = False)
    # specialization3 = db.Column(db.String(50), nullable = False)
    # summary = db.Column(db.String(200), nullable = False)
    # linkedin =   db.Column(db.String(200), unique = True)
    # facebook =  db.Column(db.String(200), unique = True)
    # instagram =  db.Column(db.String(200), unique = True)
    # profile_photo = db.Column(db.Integer,db.ForeignKey('lawyer_profile_pictures.id'), nullable = False)
    password =  db.Column(db.String(50), nullable = False)

class User_profile_pictures(db.Model):

    id = db.Column(db.Integer , primary_key = True)
    image = db.Column(db.String(200))

class Lawyer_profile_pictures(db.Model):
    
    id = db.Column(db.Integer , primary_key = True)
    image = db.Column(db.String(200))

class Lawyer_case(db.Model):
    # address,telephone and faxnumbers,emailaddress, the names of opposing parties  , and key dates , conflict-searches
    id = db.Column(db.Integer , primary_key = True)
    plaintiff = db.Column(db.String(200), unique = True)




    






    




