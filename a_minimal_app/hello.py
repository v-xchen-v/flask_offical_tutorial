# flask --app hello run
# As a shortcut, if the file is named app.py or wsgi.py, you don’t have to use --app.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"