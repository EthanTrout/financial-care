from flask import render_template
from financialcare import app, db
from financialcare.models import User,Service , user_service


@app.route("/")
def login():
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("base.html")