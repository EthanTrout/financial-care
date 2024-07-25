from flask import render_template
from financialcare import app, db


@app.route("/")
def login():
    return render_template("login.html")