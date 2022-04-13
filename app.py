# importing flask
from flask import Flask, render_template, request



app = Flask(__name__)

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
    # checking for the name
    if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        return render_template("failure.html")
    return render_template("register.html")
