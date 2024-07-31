from flask import render_template, request, redirect, url_for
from financialcare import app, db
from financialcare.models import Staff,Service , staff_service


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
    
@app.route("/users")
def users():
    staff =list(Staff.query.order_by(Staff.name).all())
    return render_template("users.html",staff=staff)


@app.route("/add_user",methods=["GET","POST"])
def add_user():
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

# @app.route("/add_user", methods=["GET", "POST"])
# def add_user():
#     services = list(Service.query.order_by(Service.name).all())
#     if request.method == "POST":
#         user_name = request.form.get("user_name")
#         email = request.form.get("email")
#         access = request.form.get("access")
#         password = request.form.get("password")
#         service_id = request.form.get("service")

#         print(f"Received form data: user_name={user_name}, email={email}, access={access}, password={password}, service_id={service_id}")

#         user = User(
#             name=user_name,
#             email=email,
#             access=access,
#         )
#         user.set_password(password)

#         try:
#             db.session.add(user)
#             db.session.commit()
#             print(f"User {user_name} added successfully with ID: {user.id}")
#         except Exception as e:
#             print(f"Error adding user: {e}")
#             db.session.rollback()
#             return "Error adding user", 500
        
#         user_service = Service.query.filter_by(id=service_id).first()
#         print(f"Queried user_service: {user_service}")

#         # if user_service is not None:
#         #     try:
#         #         user.services.append(user_service)
#         #         db.session.add(user)
#         #         db.session.commit()
#         #         print(f"Service {user_service.name} appended to user {user.name}")
#         #     except Exception as e:
#         #         print(f"Error appending service to user: {e}")
#         #         db.session.rollback()
#         #         return "Error associating service with user", 500
            
#         #     return redirect(url_for("users"))
#         # else:
#         #     print("Service not found.", "error")
        
#         return redirect(url_for("users"))
#     return render_template("add_user.html", services=services)