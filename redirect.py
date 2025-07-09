from flask import Flask,render_template,redirect,url_for
app=Flask(__name__)

@app.route('/old')
def old():
    return redirect(url_for('new'))

@app.route('/new')
def new():
    return "This is the new page"

@app.route('/')
def index():
    return render_template('indexcookie.html')

if __name__=='__main__':
    app.run(debug=True)