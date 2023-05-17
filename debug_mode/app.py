# flask run --debug
# To enable debug mode, use the --debug option.
# notice: the flask backend and browser is decoupled, so that when code is changed, in debug mode the server will automatically restart, but browser should fresh manually to see the changes.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

# a case with mismatch the function parameter name with the route
# without --debug,
# Internal Server Error
# The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application

# with --debug, show the detail error information for debugging
# TypeError
# TypeError: show_subpath() got an unexpected keyword argument 'sub_path'
@app.route('path/subpath')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'