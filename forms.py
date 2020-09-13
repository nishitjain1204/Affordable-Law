from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField,BooleanField,FileField,FormField
from wtforms.validators import DataRequired, Length, Email, EqualTo , URL

class RegistrationForm(FlaskForm):
	username= StringField('Username', validators=[DataRequired(),Length(min=2,max=25)])

	email= StringField('Email', validators=[DataRequired(), Email()])
	password= PasswordField('Password', validators=[DataRequired(),Length(min=2,max=25)])

	confirm_password= PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField('Sign up')
class ProfileForm(FlaskForm):
	FirstName= StringField('First Name', validators=[DataRequired(),Length(min=2,max=25)])
	LastName= StringField('Last Name', validators=[DataRequired(),Length(min=2,max=25)])
	location=StringField('City',validators=[DataRequired(),Length(min=2,max=20)])
	CurrentJob=StringField('Title / Position')
	Notworking=BooleanField('Open for Cases')
	Linkedin=StringField('Linkedin',validators=[URL()])
	Facebook=StringField('Facebook',validators=[URL()])
	Instagram=StringField('Instagram',validators=[URL()])
	MinFee=IntegerField('Minimum Fee',validators=[DataRequired()])
	MaxFee=IntegerField('Maximum Fee',validators=[DataRequired()])
	FirstSpec=StringField('Specialization 1',validators=[DataRequired()])
	SecSpec=StringField('Specialization 2')
	ThirdSpec=StringField('Specialization 3')
	Bio=StringField('Bio', validators=[DataRequired(),Length(min=2,max=200)])
	Number=IntegerField('Phone Number',validators=[DataRequired()])
	Profilephoto=FileField('Profile Photo')
	
	Educational_qualif_1 = StringField('Educational Qualification 1', validators=[Length(min=2,max=200)])
	Educational_Institution_1 = StringField('Educational Institution', validators=[Length(min=2,max=200)])
	From_1 = StringField('From')
	To_1 = StringField('To')

	Educational_qualif_2 = StringField('Educational Qualification 2', validators=[Length(min=2,max=200)] )
	Educational_Institution_2 = StringField('Educational Institution', validators=[Length(min=2,max=200)])
	From_2 = StringField('From',)
	To_2 = StringField('To')

	Educational_qualif_3 = StringField('Educational Qualification 3', validators=[Length(min=2,max=200)])
	Educational_Institution_3 = StringField('Educational Institution', validators=[Length(min=2,max=200)])
	From_3 = StringField('From')
	To_3 = StringField('To')

	Prof_qualif_1 = StringField('Proffesional Qualification 1', validators=[Length(min=0,max=200)])
	Institution_1 = StringField('Institution', validators=[Length(min=0,max=200)])
	From_prof_1 = StringField('From')
	To_prof_1 = StringField('To')

	Prof_qualif_2 = StringField('Proffesional Qualification 2', validators=[Length(min=0,max=200)])
	Institution_2 = StringField('Institution', validators=[Length(min=0,max=200)])
	From_prof_2 = StringField('From')
	To_prof_2 = StringField('To')

	Prof_qualif_3 = StringField('Proffesional Qualification 3', validators=[Length(min=0,max=200)])
	Institution_3 = StringField('Institution', validators=[Length(min=0,max=200)])
	From_prof_3 = StringField('From')
	To_prof_3 = StringField('To')

	
	#Resume=FileField(u'Resume', [validators.regexp(u'^[^/\\]\.jpg$')])
	Submit=SubmitField()

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
