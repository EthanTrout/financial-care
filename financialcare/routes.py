from flask import render_template, request, redirect, url_for
from financialcare import app, db
from financialcare.models import User,Service , user_service


@app.route("/")
def login():
    return render_template("login.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/add_service",methods=["GET","POST"])
def add_service():
    if request.method=="POST":
        service = Service(name=request.form.get("service_name"))
        db.session.add(service)
        db.session.commit()
        return redirect(url_for("services"))
    return render_template("add_service.html")