from flask import render_template, request, redirect, url_for, session
from financialcare import app, db
from financialcare.models import Staff,Service , staff_service


@app.route("/",methods=["GET", "POST"])
def login():
    if request.method =="POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        staff = Staff.query.filter_by(email=email).first()
        
        if staff and staff.check_password(password):
            session["user"] = staff.id
            session["user_access"] = staff.access
            return redirect(url_for("services"))
    if "user" in session:
        return redirect(url_for("services"))
    return render_template("login.html")

@app.route("/services")
def services():
    if "user" in session:
        services =list(Service.query.order_by(Service.name).all())
        return render_template("services.html",services=services)
    else:
        return redirect(url_for("login"))

@app.route("/add_service",methods=["GET","POST"])
def add_service():
    if ("user" in session) and (session["user_access"]in ["manager", "it"]):
        print(session["user_access"])
        if request.method=="POST":
            service = Service(name=request.form.get("service_name"))
            db.session.add(service)
            db.session.commit()
            return redirect(url_for("services"))
        return render_template("add_service.html")
    else:
        return redirect(url_for("login"))

@app.route("/edit_service/<int:service_id>",methods=["GET","POST"])
def edit_service(service_id):
    service = Service.query.get_or_404(service_id)
    if ("user" in session) and (session["user_access"]in ["manager", "it"]):
        if request.method == "POST":
            service.name = request.form.get("service_name")
            db.session.commit()
            return redirect(url_for("services"))
        return render_template("edit_service.html",service=service)
    else:
        return redirect(url_for("login"))

@app.route("/edit_service_staff/<int:service_id>",methods=["GET","POST"])
def edit_service_staff(service_id):
    service = Service.query.get_or_404(service_id)
    if ("user" in session) and (session["user_access"]in ["manager", "it"]):
        staff =list(Staff.query.order_by(Staff.name).all())
        if request.method == "POST":
            service.name = service.name
            print (service.name)
            staff_id = request.form.get("staff")
            service_staff = Staff.query.filter_by(id=staff_id).first()
            service.staff.append(service_staff)
            db.session.commit()
            return redirect(url_for("services"))
        return render_template("edit_service_staff.html",service=service,staff=staff)
    else:
        return redirect(url_for("login"))

@app.route("/delete_service/<int:service_id>")
def delete_service(service_id):
    if ("user" in session) and (session["user_access"]in ["manager", "it"]):
        service = Service.query.get_or_404(service_id)
        db.session.delete(service)
        db.session.commit()
        return redirect(url_for("services"))
    else:
        return redirect(url_for("login"))
    
@app.route("/users")
def users():
    if ("user" in session): #and (session["user_access"]in ["manager", "it"]):
        staff =list(Staff.query.order_by(Staff.name).all())
        return render_template("users.html",staff=staff)
    else:
        return redirect(url_for("login"))

@app.route("/add_user",methods=["GET","POST"])
def add_user():
    if ("user" in session): #and (session["user_access"]in ["manager", "it"]):
        services =list(Service.query.order_by(Service.name).all())
        if request.method=="POST":
            staff = Staff(
                name=request.form.get("user_name"),
                email=request.form.get("email"),
                access=request.form.get("access"),
                # password=request.form.get("password")
            )
            staff.set_password(request.form.get("password"))
            
            service_id = request.form.get("service")
            staff_service = Service.query.filter_by(id=service_id).first()
            print(service_id)
            # db.session.add(user)
            # db.session.commit()
            
            if staff_service is not None:
                staff.services.append(staff_service)
                db.session.add(staff)
                db.session.commit()
                return redirect(url_for("users"))
            else:
                # Handle the case where the service is not found
                db.session.add(staff)
                db.session.commit()
                return redirect(url_for("users"))
            return redirect(url_for("users"))
        return render_template("add_user.html",services=services)
    else:
        return redirect(url_for("login"))


@app.route("/edit_user/<int:staff_id>",methods=["GET","POST"])
def edit_user(staff_id):
    if ("user" in session) and (session["user_access"]in ["manager", "it"]):
        staff = Staff.query.get_or_404(staff_id)
        services =list(Service.query.order_by(Service.name).all())
        if request.method=="POST":

            staff.name=request.form.get("user_name")
            staff.email=request.form.get("email")
            staff.access=request.form.get("access")
            staff.password= staff.password
            db.session.commit()
            return redirect(url_for("users"))
            
        return render_template("edit_user.html",staff=staff,services=services)
    else:
        return redirect(url_for("login"))


@app.route("/edit_user_password/<int:staff_id>",methods=["GET","POST"])
def edit_user_password(staff_id):
    if ("user" in session) and (session["user_access"]in ["manager", "it"]):
        staff = Staff.query.get_or_404(staff_id)
        if request.method=="POST":

            staff.name= staff.name
            staff.email= staff.email
            staff.access= staff.access
            staff.set_password(request.form.get("password"))
            db.session.commit()
            return redirect(url_for("users"))
            
        return render_template("edit_user_password.html",staff=staff,services=services)
    else:
        return redirect(url_for("login"))


@app.route("/delete_user/<int:staff_id>")
def delete_user(staff_id):
    if ("user" in session) and (session["user_access"]in ["manager", "it"]):
        staff = Staff.query.get_or_404(staff_id)
        db.session.delete(staff)
        db.session.commit()
        return redirect(url_for("users"))
    else:
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    session.pop("user",None)
    session.pop("user_access",None)
    return redirect(url_for("login"))