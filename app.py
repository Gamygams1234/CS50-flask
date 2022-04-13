# importing flask
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///froshims.db'

# initialize the database
db = SQLAlchemy(app)

#Create DB Model

class User(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    name= db.Column(db.String(200), nullable = False)
    sport= db.Column(db.String(200), nullable = False)

# function to return a string when we addsomething
    def __repr__(self):
        return '<Name %r>' % self.id

SPORTS = [
    "Dodgeball",
    "Flag Footall",
    "Baseball",
    "Basketball"
]



@app.route("/")
def index():
    return render_template("index.html", sports= SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")
    sport = request.form.get("sport") 

    if not sport:
        return render_template("error.html", message = "Missing Sport" )
    if sport not in SPORTS:
        return render_template("error.html", message = "The sport is not available")

    registrant = User(name=name, sport=sport)
    # push to db
    try:
        db.session.add(registrant)
        db.session.commit()
        return redirect("/registrants")
    except: 
        return render_template("error.html", message = "There was an error adding the user" )


@app.route("/registrants", methods=["POST", "GET"])
def regisrants():
    regisrants = User.query.order_by(User.id)
    return render_template("register.html", registrants= regisrants)
