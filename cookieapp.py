from flask import Flask,make_response,request,render_template
app=Flask(__name__)
##Selecting a cookie##

@app.route('/setcookie')
def set_cookie():
    resp=make_response("Cookie has been set!")
    resp.set_cookie('username','Komal')
    return resp

#Reading a cookie##
@app.route('/getcookie')
def get_cookie():
    username=request.cookies.get('username')
    return f'Hello {username}'

##deleting a cookie
@app.route('/delcookie')
def del_cookie():
    resp=make_response("Cookie has been deleted!")
    resp.set_cookie('username','',expires=0)
    return resp

@app.route('/')
def index():
    return render_template('indexcookie.html')

if __name__== '__main__':
    app.run(debug=True)

