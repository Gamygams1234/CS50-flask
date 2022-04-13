# importing flask
from flask import Flask, render_template, request



# this current file will be an application 
# like the main method
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        return render_template("greet.html", name=request.form.get("name", "world"))


