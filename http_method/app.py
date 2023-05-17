from flask import request, Flask

app = Flask(__name__)
def do_the_login():
    return 'do the login'

def show_the_login_form():
    return 'show to login form'

# By default, a route only answers to GET requests. You can use the methods argument of the route() decorator to handle different HTTP methods.
@app.route('/login_in_one', methods=['GET', 'POST'])
def login_in_one():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.route('/login')
def login_get():
    return show_the_login_form()

# post() is shortcut for route() with methods=["POST"], but somehow it's not working sometimes.
@app.route('/login', methods=['POST'])
# @app.route('/login')
def login_post():
    return do_the_login()
