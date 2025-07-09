from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

#---------------------------------
#Step1: App and db configuration
#---------------------------------

app=Flask(__name__)

#configuration SQLlite db(students.db will be created in our project folder)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #To supress a warning

#Initializing the database object
db=SQLAlchemy(app)

#----------------------------
#step2:Define a model(Table)
#----------------------------

class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True)#Auto incrementing ID
    name=db.Column(db.String(100),nullable=False)#Student name=required
    email=db.Column(db.String(100),unique=True,nullable=False)#Email(Must be unique)

#------------------------------------
#Step3:Route to Add a student Record
#------------------------------------

@app.route('/add')
def add_student():
    student=Student(name='Komal',email='komal@example.com')
    db.session.add(student)
    db.session.commit()
    return "Student added to our database!"

#-----------------------------------------
#Step4: Route to view all Student records
#-----------------------------------------

@app.route('/students')
def list_students():
    students=Student.query.all()
    return '<br>'.join([f"{s.id}.{s.name}-{s.email}" for s in students])

#--------------------------------
#Step5:Home page route(Optional)
#--------------------------------

@app.route('/')
def home():
    return render_template('index.html')

#----------------------------------------
#Step6:Run the application and create DB
#----------------------------------------

if __name__=='__main__':
    #Creating the db and table(if not already created)
    with app.app_context():
        db.create_all()
    app.run(debug=True)