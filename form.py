'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name=StringField('Enter your name',validators=[DataRequired()])
    submit=SubmitField('Submit')
'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SelectField, BooleanField,SubmitField
from wtforms.validators import DataRequired,Email

class RegistrationForm(FlaskForm):
    name=StringField("Full  Name",validators=[DataRequired()])
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    gender=RadioField("Gender",choices=[('M','Male'),('F','Female')])
    country=SelectField("Country",choices=[('np','Nepal'),('Ch','China')])
    agree=BooleanField("I accept the terms and conditions",validators=[DataRequired()])
    submit=SubmitField("register")