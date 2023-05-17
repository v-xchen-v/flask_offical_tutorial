from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# use <converter:variable_name> to specified we expected a path type user input as url parameter so that slashes also accepted 
# visit http://localhost:5000/hello/<script>alert('Hi')</script> in browser
# the script will be run in the user's browser, it's not safe, that's why escape() shown here.

@app.route('/<path:name>')
def hello(name):
    return f'Hello, {name}!'

# visit http://localhost:5000/hello/<script>alert('Hi')</script> in browser
# escaping causes it to be rendered as text, rather than running the script in the user’s browser.
@app.route('/fix/<path:name>')
def hello_fix(name):
    return f'Hello, {escape(name)}!'
