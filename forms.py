from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField,BooleanField,FileField,FormField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	username= StringField('Username', validators=[DataRequired(),Length(min=2,max=25)])

	email= StringField('Email', validators=[DataRequired(), Email()])
	password= PasswordField('Password', validators=[DataRequired(),Length(min=2,max=25)])

	confirm_password= PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField('Sign up')
class ProfileForm(FlaskForm):
	FirstName= StringField('Firstname', validators=[DataRequired(),Length(min=2,max=25)])
	LastName= StringField('Lastname', validators=[DataRequired(),Length(min=2,max=25)])
	location=StringField('location',validators=[DataRequired()])
	CurrentJob=StringField('CurrentJob')
	Notworking=BooleanField('Notworking')
	Linkedin=StringField('Linkedin')
	MinFee=IntegerField('Minimumfee',validators=[DataRequired()])
	MaxFee=IntegerField('Maximumfee',validators=[DataRequired()])
	FirstSpec=StringField('Specialization 1',validators=[DataRequired()])
	SecSpec=StringField('Specialization 2')
	ThirdSpec=StringField('Specialization 3')
	Bio=StringField('Bio', validators=[DataRequired(),Length(min=2,max=200)])
	country_code=IntegerField('Country Code',validators=[DataRequired()])
	area_code= IntegerField('AreaCode',validators=[DataRequired()])
	number=IntegerField('PhoneNumber',validators=[DataRequired()])
	#image=FileField(u'Image File', [validators.regexp(u'^[^/\\]\.jpg$')])
	#Resume=FileField(u'Resume', [validators.regexp(u'^[^/\\]\.jpg$')])
	submit=SubmitField('Create')

class LoginForm(FlaskForm):
	email= StringField('Email', validators=[DataRequired(), Email()])
	password= PasswordField('Password', validators=[DataRequired(),Length(min=2,max=25)])
	remember = BooleanField('remember me')
	submit=SubmitField('Sign in')

class File_upload(FlaskForm):
	case_file = FileField('Case File')
    	

class CaseForm(FlaskForm):
	Name= StringField('Name', validators=[DataRequired(),Length(min=2,max=25)])
	Day=IntegerField('Day (Eg: 01)',validators=[DataRequired()])
	Month=IntegerField('Month (Eg:01 for Jan)',validators=[DataRequired()])
	Year=IntegerField('Month (Eg:2001)',validators=[DataRequired()])
	Bio=StringField('Summary of case ', validators=[DataRequired(),Length(min=2,max=200)])
	case_file = FileField('Case File')
	submit=SubmitField()
