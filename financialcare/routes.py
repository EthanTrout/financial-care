from flask import render_template, request, redirect, url_for
from financialcare import app, db
from financialcare.models import User,Service , user_service


@app.route("/")
def login():
    return render_template("login.html")

@app.route("/services")
def services():
    services =list(Service.query.order_by(Service.name).all())
    return render_template("services.html",services=services)

@app.route("/add_service",methods=["GET","POST"])
def add_service():
    if request.method=="POST":
        service = Service(name=request.form.get("service_name"))
        db.session.add(service)
        db.session.commit()
        return redirect(url_for("services"))
    return render_template("add_service.html")

@app.route("/edit_service/<int:service_id>",methods=["GET","POST"])
def edit_service(service_id):
    service = Service.query.get_or_404(service_id)
    if request.method == "POST":
        service.name = request.form.get("service_name")
        db.session.commit()
        return redirect(url_for("services"))
    return render_template("edit_service.html",service=service)

@app.route("/delete_service/<int:service_id>")
def delete_service(service_id):
    service = Service.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    return redirect(url_for("services"))
    
