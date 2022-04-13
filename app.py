# importing flask
from flask import Flask, render_template, request



app = Flask(__name__)

SPORTS = [
    "Dodgeball",
    "Flag Footall",
    "Baseball",
    "Basketball"
]

REGISTRANTS = {

}

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
        return render_template("error.html")

    REGISTRANTS[name] = sport
    return render_template("register.html", registrants= REGISTRANTS)
