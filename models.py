
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import UserMixin

# from main import app 
db = SQLAlchemy()



class User(UserMixin, db.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here

    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(50), nullable = False,unique=True)
    email_id  = db.Column(db.String(200), nullable = False , unique = True)
    password =  db.Column(db.String(50), nullable = False)


class Lawyer(UserMixin,db.Model):

    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(50), nullable = False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email_id  = db.Column(db.String(200), nullable = False, unique = True)
    current_job = db.Column(db.String(50))
    open_for_cases=db.Column(db.Boolean())
    city =  db.Column(db.String(50))
    specialization1 = db.Column(db.String(50))
    specialization2 = db.Column(db.String(50))
    specialization3 = db.Column(db.String(50))
    bio = db.Column(db.String(200))
    linkedin =   db.Column(db.String(200), unique = True)
    facebook =  db.Column(db.String(200), unique = True)
    instagram =  db.Column(db.String(200), unique = True)
    min_fee= db.Column(db.Integer)
    max_fee= db.Column(db.Integer)
    profile_photo = db.Column(db.String(200) , unique=True)
    phone_number = db.Column(db.Integer , unique=True)


    password =  db.Column(db.String(50), nullable = False)
    cases  = db.relationship('Lawyer_case', backref = 'lawyer')
    educational_qualif_1  = db.relationship('Lawyer_educational_qualif_1', uselist=False, backref = 'lawyer')
    educational_qualif_2  = db.relationship('Lawyer_educational_qualif_2',uselist=False, backref = 'lawyer')
    educational_qualif_3  = db.relationship('Lawyer_educational_qualif_3',uselist=False, backref = 'lawyer')
    proffesional_qualif_1 = db.relationship('Lawyer_prof_qualif_1',uselist=False, backref = 'lawyer')
    proffesional_qualif_2 = db.relationship('Lawyer_prof_qualif_2', uselist=False,backref = 'lawyer')
    proffesional_qualif_3 = db.relationship('Lawyer_prof_qualif_3',uselist=False, backref = 'lawyer')
   

class User_profile_pictures(db.Model):

    id = db.Column(db.Integer , primary_key = True)
    user_image_path = db.Column(db.String(200))


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

class Lawyer_prof_qualif_1(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    prof_institute=db.Column(db.String(200))
    prof_qualif=db.Column(db.String(200))
    from_prof=db.Column(db.String(10))
    to_prof=db.Column(db.String(10))
    lawyer_id = db.Column(db.Integer , db.ForeignKey('lawyer.id')) 

class Lawyer_prof_qualif_2(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    prof_qualif=db.Column(db.String(200))
    prof_institute=db.Column(db.String(200))
    from_prof=db.Column(db.String(10))
    to_prof=db.Column(db.String(10))
    lawyer_id = db.Column(db.Integer , db.ForeignKey('lawyer.id')) 

class Lawyer_prof_qualif_3(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    prof_qualif=db.Column(db.String(200))
    prof_institute=db.Column(db.String(200))
    from_prof=db.Column(db.String(10))
    to_prof=db.Column(db.String(10))
    lawyer_id = db.Column(db.Integer , db.ForeignKey('lawyer.id')) 
    
class Lawyer_educational_qualif_1(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    educational_qualif=db.Column(db.String(200))
    educational_institute=db.Column(db.String(200))
    from_=db.Column(db.String(10))
    to_=db.Column(db.String(10))
    lawyer_id = db.Column(db.Integer , db.ForeignKey('lawyer.id')) 



class Lawyer_educational_qualif_2(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    educational_qualif=db.Column(db.String(200))
    educational_institute=db.Column(db.String(200))
    from_=db.Column(db.String(10))
    to_=db.Column(db.String(10))
    lawyer_id = db.Column(db.Integer , db.ForeignKey('lawyer.id')) 


class Lawyer_educational_qualif_3(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    educational_qualif=db.Column(db.String(200))
    educational_institute=db.Column(db.String(200))
    from_=db.Column(db.String(10))
    to_=db.Column(db.String(10))
    lawyer_id = db.Column(db.Integer , db.ForeignKey('lawyer.id')) 







    






    




