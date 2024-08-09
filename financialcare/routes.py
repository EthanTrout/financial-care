from flask import render_template, request, redirect, url_for, session
from financialcare import app, db
from financialcare.models import Staff,Service , staff_service, ServiceUser, WalletEntry
from datetime import datetime
from decimal import Decimal



# Login logout routes
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


@app.route("/logout")
def logout():
    session.pop("user",None)
    session.pop("user_access",None)
    return redirect(url_for("login"))


# Service routes
@app.route("/services")
def services():
    if "user" in session:
        if session["user_access"]in ["manager", "it"]:
            services =list(Service.query.order_by(Service.name).all())
            return render_template("services.html",services=services)
        elif session["user_access"] == "support":
            staff = Staff.query.filter_by(id=session["user"]).first()
            service_ids =[]
            for service in staff.services:
                service_ids.append(service.id)
            print(service_ids)
            services = Service.query.filter(Service.id.in_(service_ids)).all()
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

# Staff/website user routes

@app.route("/users")
def users():
    if ("user" in session) and (session["user_access"]in ["manager", "it"]):
        staff =list(Staff.query.order_by(Staff.name).all())
        return render_template("users.html",staff=staff)
    else:
        return redirect(url_for("login"))

@app.route("/add_user",methods=["GET","POST"])
def add_user():
    if ("user" in session) and (session["user_access"]in ["manager", "it"]):
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
    
# Indivdual/ service_user routes 

@app.route("/individual")
def service_users():
    if "user" in session:
        if session["user_access"]in ["manager", "it"]:
            service_users =list(ServiceUser.query.order_by(ServiceUser.name).all())
            return render_template("service_users.html",service_users=service_users)
        elif session["user_access"] == "support":
            # service_users =list(ServiceUser.query.order_by(ServiceUser.name).all())
            staff = Staff.query.filter_by(id=session["user"]).first()
            service_ids =[]
            for service in staff.services:
                service_ids.append(service.id)
            print(service_ids)
            service_users = ServiceUser.query.filter(ServiceUser.service_id.in_(service_ids)).all()
            return render_template("service_users.html",service_users=service_users)
    else:
        return redirect(url_for("login"))

@app.route("/individual<int:service_id>")
def service_users_in_service(service_id):
    if "user" in session:
        service_users = ServiceUser.query.filter_by(service_id=service_id).all()
        return render_template("service_users.html",service_users=service_users)
    else:
        return redirect(url_for("login"))

@app.route("/add_individual",methods=["GET","POST"])
def add_service_user():
    services =list(Service.query.order_by(Service.name).all())
    if ("user" in session) and (session["user_access"]in ["manager", "it"]):
        if request.method=="POST":
                service_user = ServiceUser(
                    name=request.form.get("name"),
                    bank=request.form.get("bank"),
                    service_id=request.form.get("service")
                    )
                db.session.add(service_user)
                db.session.commit()
                return redirect(url_for("service_users"))
            
        return render_template("add_service_user.html",services=services)
    else:
        return redirect(url_for("login"))


@app.route("/edit_individual/<int:service_user_id>",methods=["GET","POST"])
def edit_service_user(service_user_id):
    service_user = ServiceUser.query.get_or_404(service_user_id)
    if ("user" in session) and (session["user_access"]in ["manager", "it"]):
        services =list(Service.query.order_by(Service.name).all())
        if request.method == "POST":
            service_user.name = request.form.get("name")
            service_user.bank = request.form.get("bank")
            service_user.service_id = request.form.get("service")
            db.session.commit()
            return redirect(url_for("service_users"))
        return render_template("edit_service_user.html",service_user=service_user,services=services)
    else:
        return redirect(url_for("login"))

@app.route("/delete_individual/<int:service_user_id>")
def delete_service_user(service_user_id):
    if ("user" in session) and (session["user_access"]in ["manager", "it"]):
        service_user = ServiceUser.query.get_or_404(service_user_id)
        db.session.delete(service_user)
        db.session.commit()
        return redirect(url_for("service_users"))
    else:
        return redirect(url_for("login"))


# Wallet routes
@app.route("/open_wallet/<int:service_user_id>",methods=["GET","POST"])
def open_wallet(service_user_id):
    service_user = ServiceUser.query.get_or_404(service_user_id)
    last_wallet_entry = WalletEntry.query.filter_by(service_user_id=service_user_id).order_by(WalletEntry.id.desc()).first()
    if last_wallet_entry is None:
        return redirect(url_for("set_up_wallet",service_user_id=service_user_id))

    if last_wallet_entry.cash_out > 0 or last_wallet_entry.bank_card_removed == True:
        return redirect(url_for("close_wallet",service_user_id=service_user_id,last_wallet_id=last_wallet_entry.id,outstanding_money=last_wallet_entry.cash_out))

    
    if request.method == "POST":
        wallet_entry = WalletEntry(
            service_user_id = service_user.id,
            staff_id = session["user"],
            date_time = datetime.now(),
            seal_number = request.form.get("seal_number"),
            cash_amount = last_wallet_entry.cash_amount - float(request.form.get("cash_out")),
            bank_amount = last_wallet_entry.bank_amount,
            cash_out = float(request.form.get("cash_out")),
            cash_in = 0,
            bank_card_removed = bool(request.form.get("bank_card_removed")),
            money_spent = 0,
            money_spent_description = request.form.get("cash_out_description"),
            bank_out = 0 ,
            bank_in = 0,
            receipt_number = 0
            )
        db.session.add(wallet_entry)
        db.session.commit()
        print((bool(request.form.get("bank_card_removed"))))
        return redirect(url_for("services"))
    else:
        return render_template("open_wallet.html",service_user=service_user)
            



@app.route("/close_wallet/<int:service_user_id>/<int:last_wallet_id>/<float:outstanding_money>",methods=["GET","POST"])
def close_wallet(service_user_id,last_wallet_id,outstanding_money):
    service_user = ServiceUser.query.get_or_404(service_user_id)
    last_wallet_entry = WalletEntry.query.filter_by(id=last_wallet_id).first()
    outstanding_money = Decimal(str(outstanding_money))
    last_entry_with_receipt = WalletEntry.query.filter(WalletEntry.receipt_number != 0).order_by(WalletEntry.id.desc()).first()
    if request.method == "POST":
        print(outstanding_money)
        if outstanding_money >= float(request.form.get("money_spent")):
            if last_entry_with_receipt is not None:
                receipt_number = last_entry_with_receipt.receipt_number + 1
            else:
                receipt_number = 1
            wallet_entry = WalletEntry(
                service_user_id = service_user.id,
                staff_id = session["user"],
                date_time = datetime.now(),
                seal_number = last_wallet_entry.seal_number,
                cash_amount = last_wallet_entry.cash_amount,
                bank_amount = last_wallet_entry.bank_amount,
                cash_out = 0,
                cash_in = 0,
                bank_card_removed= last_wallet_entry.bank_card_removed,
                money_spent = float(request.form.get("money_spent")),
                money_spent_description = request.form.get("money_spent_description"),
                bank_out = 0 ,
                bank_in = 0,
                receipt_number = receipt_number
                )
            db.session.add(wallet_entry)
            db.session.commit()
            money_spent = Decimal(request.form.get("money_spent"))
            new_outstanding_money = outstanding_money - money_spent
            return redirect(url_for("close_wallet",service_user_id = service_user_id,last_wallet_id=last_wallet_id,outstanding_money=float(new_outstanding_money)))
        else:
            return("not enough money out to add")
    else:
        return render_template("close_wallet.html",service_user=service_user,last_wallet_id=last_wallet_id,outstanding_money=outstanding_money)


@app.route("/close_wallet_add_cash/<int:service_user_id>/<int:last_wallet_id>/<float:outstanding_money>",methods=["GET","POST"])
def close_wallet_add_cash(service_user_id,last_wallet_id,outstanding_money):
    # Add cash back into wallet 
    service_user = ServiceUser.query.get_or_404(service_user_id)
    last_wallet_entry = WalletEntry.query.filter_by(id=last_wallet_id).first()
    show_modal = False
    remaining_money = 0
    print(outstanding_money)
    if request.method == "POST":
        cash_in = float(request.form.get("cash_in"))
        if cash_in == outstanding_money:
            wallet_entry = WalletEntry(
                service_user_id=service_user.id,
                staff_id=session["user"],
                date_time=datetime.now(),
                seal_number=request.form.get("seal_number"),
                cash_amount=last_wallet_entry.cash_amount + cash_in,
                bank_amount=last_wallet_entry.bank_amount,
                cash_out=0,
                cash_in=cash_in,
                bank_card_removed=False,
                money_spent=0,
                money_spent_description="Remaining cash back in",
                bank_out = 0 ,
                bank_in = 0,
                receipt_number = 0
            )
            db.session.add(wallet_entry)
            db.session.commit()
            if last_wallet_entry.bank_card_removed:
                return redirect(url_for("close_wallet_banking",service_user_id=service_user_id))
            return redirect(url_for("services"))
        else:
            show_modal = True
            remaining_money = outstanding_money - cash_in

    return render_template("close_wallet_add_cash.html", service_user=service_user, last_wallet_id=last_wallet_id, outstanding_money=outstanding_money, show_modal=show_modal,remaining_money=remaining_money)
    #  if cash doesnt add up to total then propmpt to call manager or review reciepts
    

@app.route("/close_wallet_banking/<int:service_user_id>",methods=["GET","POST"])
def close_wallet_banking(service_user_id):
    service_user = ServiceUser.query.get_or_404(service_user_id)
    last_wallet_entry = WalletEntry.query.filter_by(service_user_id=service_user_id).order_by(WalletEntry.id.desc()).first()
    last_entry_with_receipt = WalletEntry.query.filter(WalletEntry.receipt_number != 0).order_by(WalletEntry.id.desc()).first()
    if request.method == "POST":
        if last_entry_with_receipt is not None:
            receipt_number = last_entry_with_receipt.receipt_number + 1
        else:
            receipt_number = 1
        wallet_entry = WalletEntry(
            service_user_id = service_user.id,
            staff_id = session["user"],
            date_time = datetime.now(),
            seal_number = last_wallet_entry.seal_number,
            cash_amount = last_wallet_entry.cash_amount,
            bank_amount = last_wallet_entry.bank_amount - float(request.form.get("bank_out")),
            cash_out = 0,
            cash_in = 0,
            bank_card_removed=bool(False),
            money_spent = float(request.form.get("bank_out")),
            money_spent_description = request.form.get("money_spent_description"),
            bank_out = float(request.form.get("bank_out")) ,
            bank_in = 0,
            receipt_number = receipt_number
            )
        db.session.add(wallet_entry)
        db.session.commit()
        return redirect(url_for("close_wallet_banking",service_user_id=service_user_id))
    else:
        return render_template("close_wallet_banking.html",service_user=service_user)


@app.route("/set_up_wallet/<int:service_user_id>",methods=["GET","POST"])
def set_up_wallet(service_user_id):
    service_user = ServiceUser.query.get_or_404(service_user_id)
    if request.method == "POST":
        wallet_entry = WalletEntry(
            service_user_id = service_user.id,
            staff_id = session["user"],
            date_time = datetime.now(),
            seal_number = request.form.get("seal_number"),
            cash_amount = request.form.get("cash_amount"),
            bank_amount = request.form.get("bank_amount"),
            cash_out = 0,
            cash_in = 0,
            bank_card_removed=bool(False),
            money_spent = 0,
            money_spent_description = "Setting up Wallet",
            bank_out = 0 ,
            bank_in = 0,
            receipt_number = 0
            )
        db.session.add(wallet_entry)
        db.session.commit()
        return redirect(url_for("services"))
    else:
        return render_template("set_up_wallet.html",service_user=service_user)
            
@app.route("/check_seal/<int:service_user_id>", methods=["GET","POST"])
def check_seal(service_user_id):
    service_user = ServiceUser.query.get_or_404(service_user_id)
    last_wallet_entry = WalletEntry.query.filter_by(service_user_id=service_user_id).order_by(WalletEntry.id.desc()).first()
    open_modal = False
    if last_wallet_entry is None:
        return redirect(url_for("open_wallet",service_user_id=service_user_id))

    if request.method == "POST":
        if last_wallet_entry.seal_number == int(request.form.get("seal_number")):
            return redirect(url_for("open_wallet",service_user_id=service_user_id))
        else:
            open_modal = True
    return render_template("check_seal.html",service_user_id=service_user_id, open_modal=open_modal)


@app.route("/view_wallet/<int:service_user_id>")
def view_wallet(service_user_id):
    wallet_entries = WalletEntry.query.filter_by(service_user_id=service_user_id).order_by(WalletEntry.date_time.desc()).all()
    staff = list(Staff.query.order_by(Staff.id).all())
    return render_template("view_wallet.html",wallet_entries=wallet_entries,staff=staff)

    