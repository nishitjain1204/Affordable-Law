from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField,BooleanField,FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	username= StringField('Username', validators=[DataRequired(),Length(min=2,max=25)])

	email= StringField('Email', validators=[DataRequired(), Email()])
	password= PasswordField('Password', validators=[DataRequired(),Length(min=2,max=25)])

	confirm_password= PasswordField('Confirm Psssword', validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField('Sign up')
class ProfileForm(FlaskForm):
	FirstName= StringField('First name', validators=[DataRequired(),Length(min=2,max=25)])
	LastName= StringField('Last name', validators=[DataRequired(),Length(min=2,max=25)])
	location=StringField('location',validators=[DataRequired()])
	CurrentJob=StringField('Current Job')
	Notworking=BooleanField('Not working')
	Linkedin=StringField('Linkedin')
	MinFee=IntegerField('Minimum fee',validators=[DataRequired()])
	MaxFee=IntegerField('Maximum fee',validators=[DataRequired()])
	FirstSpec=StringField('Specialization 1',validators=[DataRequired()])
	SecSpec=StringField('Specialization 2')
	ThirdSpec=StringField('Specialization 3')
	Bio=StringField('Bio', validators=[DataRequired(),Length(min=2,max=200)])
	country_code=IntegerField('Country Code',validators=[DataRequired()])
	area_code= IntegerField('Area Code/Exchange',validators=[DataRequired()])
	number=IntegerField('Phone Number',validators=[DataRequired()])
	#image=FileField(u'Image File', [validators.regexp(u'^[^/\\]\.jpg$')])
	#Resume=FileField(u'Resume', [validators.regexp(u'^[^/\\]\.jpg$')])
	submit=SubmitField('Create')

class LoginForm(FlaskForm):
	email= StringField('Email', validators=[DataRequired(), Email()])
	password= PasswordField('Password', validators=[DataRequired(),Length(min=2,max=25)])
	remember = BooleanField('remember me')
	submit=SubmitField('Sign in')