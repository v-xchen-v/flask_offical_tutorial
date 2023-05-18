from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

def valid_login(username, password):
    if username == 'xi' and password == "123":
        return True
    else:
        return False
    
def log_the_user_in(username):
    print(f'{username} is login in.')
    return render_template('index.html')

@app.route('/login', methods=["post", "get"])
def login():
    error = None
    if request.method == "POST":
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = "invalid username/password"
        
    return render_template("index.html", error=error)