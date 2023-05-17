from flask import Flask
app = Flask(__name__)

# http://localhost:5000
@app.route('/')
def index():
    return 'Index Page'

# http://localhost:5000/hello
@app.route('/hello')
def hello():
    return 'Hello, World'