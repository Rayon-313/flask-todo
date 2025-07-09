'''
from flask import Flask, render_template

app=Flask(__name__)
@app.route('/')
def home():
    
    return render_template("index.html")

@app.route('/ncit')
def ncit():
    return 'NCIT' 
 

if __name__=="__main__":
    app.run(debug=True,port=5000)
'''
from flask import Flask, request, render_template
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    error=None
    if request.method=='POST':
        name=request.form['name'].strip()
        if not name:
            error="Name cannot be empty!"
        else:
            return f"Hello, {name}!"
    return render_template('index.html',error=error)

if __name__=="__main__":
    app.run(debug=True,port=500)