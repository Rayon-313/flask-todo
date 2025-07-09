from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SelectField, BooleanField,SubmitField
from wtforms.validators import DataRequired,Email


app=Flask(__name__)
app.secret_key='Rayon Maharjan'

class RegistrationForm(FlaskForm):
    name=StringField("Full  Name",validators=[DataRequired()])
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    gender=RadioField("Gender",choices=[('M','Male'),('F','Female')])
    country=SelectField("Country",choices=[('np','Nepal'),('Ch','China')])
    agree=BooleanField("I accept the terms and conditions",validators=[DataRequired()])
    submit=SubmitField("register")

@app.route('/',methods=['GET','POST'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        country=form.country.data
        return f"Hello, {name} from {country}, your registeration is successful!"
    

    return render_template('index1.html',form=form)

if __name__=="__main__":
    app.run(debug=True,port=5000)
