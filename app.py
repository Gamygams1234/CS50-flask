# importing flask
from flask import Flask



# this current file will be an application 
# like the main method
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"