from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL']='sqlite:///students.db'
db=SQLAlchemy(app)

@app.route('/add_multiple')
def add_multiple():
    try:
        s1=Student(name='Komal',email='komal@example.com')
        s2=Student(name='NCIT',email='ncit@example.com')
        db.session.add_all([s1,s2])
        db.session.commit()#commit only if inserts are successful
        return "Both students added successfully!"
    
    except:
        db.session.rollback()#roll back if any error occurs
        return "Error: Transaction failed!"