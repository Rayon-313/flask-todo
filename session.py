from flask import Flask,session,render_template

app= Flask(__name__)
app.secret_key='KomalYadav'

#setting session data
@app.route('/login')
def login():
    session['username']='Komal'
    return 'Logged In!'

#Accessing Session data
@app.route('/profile')
def profile():
    username=session.get('username')
    return f'Logged in as {username}'

#Removing session data
@app.route('/logout')
def logout():
    session.pop('username',None)
    return 'Logged Out!'

@app.route('/')
def index():
    return render_template('indexcookie.html')

if __name__=='__main__':
    app.run(debug=True)