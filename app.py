# importing flask
from flask import Flask, render_template, request



# this current file will be an application 
# like the main method
app = Flask(__name__)

@app.route("/")
def index():
    # the second argumant will be the default name of the function
    return render_template("index.html", name=request.args.get("name", "world"))