from flask import render_template, request, redirect, url_for, session, flash
from financialcare import app, db
from financialcare.models import Staff,Service , staff_service, ServiceUser, WalletEntry
from datetime import datetime
from decimal import Decimal
from functools import wraps


# Decorator to enforce user authentication and role-based access control.
# Redirects to the login page if the user is not logged in.
# Redirects to a designated page if the user does not have the required role to access the resource.
def login_required(allowed_roles=None):
    if allowed_roles is None:
        allowed_roles = []

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if "user" not in session:
                return redirect(url_for("login"))
            
            if session.get("user_access") not in allowed_roles:
                return redirect(url_for("services"))  # Redirect to a general page or an error page

            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Template filter to format Float as a decimal like 0.00
@app.template_filter('floatformat')
def floatformat(value, decimal_places=2):
    """Format a Decimal or float to a specific number of decimal places."""
    if isinstance(value, Decimal):
        return f"{value:.{decimal_places}f}"
    elif isinstance(value, float):
        return f"{value:.{decimal_places}f}"
    return value

# Utility processor for jinja2 to Previous Url on all routes
@app.context_processor
def utility_processor():
    def get_previous_url(default='services'):
        return request.referrer or url_for(default)
    return dict(get_previous_url=get_previous_url)


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
            if 'all_receipts' not in session:
                session['all_receipts'] = []
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
@login_required(allowed_roles=["manager", "it", "support"])
def services():
    services = []  # Default value in case none of the conditions are met
    # Clear session of reciepts
    session['all_receipts'] = []
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

@app.route("/add_service",methods=["GET","POST"])
@login_required(allowed_roles=["manager", "it"])
def add_service():
    print(session["user_access"])
    if request.method=="POST":
        service = Service(name=request.form.get("service_name"))
        db.session.add(service)
        db.session.commit()
        return redirect(url_for("services"))
    return render_template("add_service.html")
    

@app.route("/edit_service/<int:service_id>",methods=["GET","POST"])
@login_required(allowed_roles=["manager", "it"])
def edit_service(service_id):
    service = Service.query.get_or_404(service_id)
    staff_members = Staff.query.join(staff_service).join(Service).filter(Service.id == service_id).all()
    staff_info = [{"id": staff.id, "name": staff.name} for staff in staff_members]
    print(staff_members)
    if request.method == "POST":
        service.name = request.form.get("service_name")
        db.session.commit()
        return redirect(url_for("services"))
    return render_template("edit_service.html",service=service,staff_info=staff_info)


@app.route("/edit_service_staff/<int:service_id>",methods=["GET","POST"])
@login_required(allowed_roles=["manager", "it"])
def edit_service_staff(service_id):
    service = Service.query.get_or_404(service_id)
    staff =list(Staff.query.order_by(Staff.name).all())
    if request.method == "POST":
        service.name = service.name
        print (service.name)
        staff_id = request.form.get("staff")
        service_staff = Staff.query.filter_by(id=staff_id).first()
        service.staff.append(service_staff)
        db.session.commit()
        return redirect(url_for("edit_service",service_id=service_id))
    return render_template("edit_service_staff.html",service=service,staff=staff)

@app.route("/delete_service/<int:service_id>")
@login_required(allowed_roles=["manager", "it"])
def delete_service(service_id):
    service = Service.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    return redirect(url_for("services"))

@app.route("/remove_staff_from_service/<int:staff_id>/<int:service_id>")
@login_required(allowed_roles=["manager", "it"])
def remove_staff_from_service(staff_id, service_id):
    service = Service.query.get_or_404(service_id)
    staff = Staff.query.get_or_404(staff_id)

    if staff in service.staff:
        service.staff.remove(staff)
        db.session.commit()

    return redirect(url_for("edit_service", service_id=service_id))

# Staff/website user routes

@app.route("/users")
@login_required(allowed_roles=["manager", "it"])
def users():
    staff =list(Staff.query.order_by(Staff.name).all())
    return render_template("users.html",staff=staff)


@app.route("/add_user",methods=["GET","POST"])
@login_required(allowed_roles=["manager", "it"])
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


@app.route("/edit_user/<int:staff_id>",methods=["GET","POST"])
@login_required(allowed_roles=["manager", "it"])
def edit_user(staff_id):
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


@app.route("/edit_user_password/<int:staff_id>",methods=["GET","POST"])
@login_required(allowed_roles=["manager", "it"])
def edit_user_password(staff_id):
    staff = Staff.query.get_or_404(staff_id)
    if request.method=="POST":

        staff.name= staff.name
        staff.email= staff.email
        staff.access= staff.access
        staff.set_password(request.form.get("password"))
        db.session.commit()
        return redirect(url_for("users"))
            
    return render_template("edit_user_password.html",staff=staff,services=services)


@app.route("/delete_user/<int:staff_id>")
@login_required(allowed_roles=["manager", "it"])
def delete_user(staff_id):
    staff = Staff.query.get_or_404(staff_id)
    db.session.delete(staff)
    db.session.commit()
    return redirect(url_for("users"))

    
# Indivdual/ service_user routes 

@app.route("/individual")
@login_required(allowed_roles=["manager", "it","support"])
def service_users():
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


@app.route("/individual/<int:service_id>")
@login_required(allowed_roles=["manager", "it","support"])
def service_users_in_service(service_id):
    service_users = ServiceUser.query.filter_by(service_id=service_id).all()
    return render_template("service_users.html",service_users=service_users)


@app.route("/add_individual",methods=["GET","POST"])
@login_required(allowed_roles=["manager", "it"])
def add_service_user():
    services =list(Service.query.order_by(Service.name).all())
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


@app.route("/edit_individual/<int:service_user_id>",methods=["GET","POST"])
@login_required(allowed_roles=["manager", "it"])
def edit_service_user(service_user_id):
    service_user = ServiceUser.query.get_or_404(service_user_id)
    services =list(Service.query.order_by(Service.name).all())
    if request.method == "POST":
        service_user.name = request.form.get("name")
        service_user.bank = request.form.get("bank")
        service_user.service_id = request.form.get("service")
        db.session.commit()
        return redirect(url_for("service_users"))
    return render_template("edit_service_user.html",service_user=service_user,services=services)


@app.route("/delete_individual/<int:service_user_id>")
@login_required(allowed_roles=["manager", "it"])
def delete_service_user(service_user_id):
    service_user = ServiceUser.query.get_or_404(service_user_id)
    db.session.delete(service_user)
    db.session.commit()
    return redirect(url_for("service_users"))



# Wallet routes
@app.route("/open_wallet/<int:service_user_id>",methods=["GET","POST"])
@login_required(allowed_roles=["manager", "it","support"])
def open_wallet(service_user_id):
    service_user = ServiceUser.query.get_or_404(service_user_id)
    last_wallet_entry = WalletEntry.query.filter_by(service_user_id=service_user_id).order_by(WalletEntry.id.desc()).first()
    if last_wallet_entry is None:
        return redirect(url_for("set_up_wallet",service_user_id=service_user_id))
    if last_wallet_entry.cash_out == 0 and last_wallet_entry.bank_card_removed == True:
        return redirect(url_for("close_wallet_banking",service_user_id=service_user_id,enter_seal = True))

    if last_wallet_entry.is_cash_removed == True :
        last_wallet_entry = WalletEntry.query.filter(
        WalletEntry.service_user_id == service_user_id,
        WalletEntry.cash_out > 0).order_by(WalletEntry.id.desc()).first()

        subsequent_entries = WalletEntry.query.filter(
        WalletEntry.service_user_id == last_wallet_entry.service_user_id,
        WalletEntry.id > last_wallet_entry.id,  
        WalletEntry.is_cash_removed == True ).all()

        if subsequent_entries:
            cash_spent_values = [entry.money_spent for entry in subsequent_entries]
            total_cash_spent = sum(cash_spent_values)
        else:
            total_cash_spent = 0
        

        result = last_wallet_entry.cash_out - total_cash_spent

        return redirect(url_for("close_wallet",service_user_id=service_user_id,last_wallet_id=last_wallet_entry.id,outstanding_money=result))

    if request.method == "POST":
        wallet_entry = WalletEntry(
            service_user_id = service_user.id,
            staff_id = session["user"],
            date_time = datetime.now(),
            seal_number = request.form.get("seal_number"),
            cash_amount = Decimal(last_wallet_entry.cash_amount) - Decimal(request.form.get("cash_out")),
            bank_amount = last_wallet_entry.bank_amount,
            cash_out = Decimal(request.form.get("cash_out")),
            cash_in = 0,
            bank_card_removed = bool(request.form.get("bank_card_removed")),
            money_spent = 0,
            money_spent_description = request.form.get("cash_out_description"),
            bank_out = 0 ,
            bank_in = 0,
            receipt_number = 0,
            is_cash_removed = True
            )
        db.session.add(wallet_entry)
        db.session.commit()
        print((bool(request.form.get("bank_card_removed"))))
        return redirect(url_for("service_users_in_service",service_id = service_user.service_id))
    else:
        return render_template("open_wallet.html",service_user=service_user)
            



@app.route("/close_wallet/<int:service_user_id>/<int:last_wallet_id>/<float:outstanding_money>",methods=["GET","POST"])
@login_required(allowed_roles=["manager", "it","support"])
def close_wallet(service_user_id,last_wallet_id,outstanding_money):
    service_user = ServiceUser.query.get_or_404(service_user_id)
    last_wallet_entry = WalletEntry.query.filter_by(id=last_wallet_id).first()
    outstanding_money = Decimal(str(outstanding_money))
    last_entry_with_receipt = (
    WalletEntry.query
    .filter(WalletEntry.receipt_number != 0)
    .filter(WalletEntry.service_user_id == service_user_id)
    .order_by(WalletEntry.id.desc())
    .first())
    show_modal = False


    # Retrieve receipts from session
    all_receipts = session.get('all_receipts', [])

    if request.method == "POST":
        money_spent = Decimal(request.form.get("money_spent"))
        if outstanding_money >= money_spent:
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
                money_spent = money_spent,
                money_spent_description = request.form.get("money_spent_description"),
                bank_out = 0 ,
                bank_in = 0,
                receipt_number = receipt_number,
                is_cash_removed = True
                )
            db.session.add(wallet_entry)
            db.session.commit()
            new_outstanding_money = outstanding_money - money_spent

             # Update receipts
            receipt = [receipt_number, request.form.get("money_spent_description"), float(money_spent)]
            all_receipts.append(receipt)

            # Store updated receipts in session
            session['all_receipts'] = all_receipts

            print(all_receipts)
            
            return redirect(url_for("close_wallet",service_user_id = service_user_id,last_wallet_id=last_wallet_id,outstanding_money=float(new_outstanding_money)))
        else:
            new_outstanding_money = outstanding_money - money_spent
            show_modal = True
            
            
    return render_template("close_wallet.html",service_user=service_user,last_wallet_id=last_wallet_id,outstanding_money=outstanding_money,all_receipts=all_receipts,show_modal =show_modal,is_card_out = last_wallet_entry.bank_card_removed )


@app.route("/close_wallet_add_cash/<int:service_user_id>/<int:last_wallet_id>/<float:outstanding_money>",methods=["GET","POST"])
@login_required(allowed_roles=["manager", "it","support"])
def close_wallet_add_cash(service_user_id,last_wallet_id,outstanding_money):
    
    service_user = ServiceUser.query.get_or_404(service_user_id)
    last_wallet_entry = WalletEntry.query.filter_by(id=last_wallet_id).first()
    show_modal = False
    remaining_money = Decimal(0.00)
    outstanding_money = Decimal(str(outstanding_money))
    print(outstanding_money)
    if request.method == "POST":
        cash_in = Decimal(request.form.get("cash_in"))
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
                receipt_number = 0,
                is_cash_removed = False
            )
            db.session.add(wallet_entry)
            db.session.commit()
            # Clear session of reciepts
            session['all_receipts'] = []
            if last_wallet_entry.bank_card_removed:
                return redirect(url_for("close_wallet_banking",service_user_id=service_user_id,enter_seal=False))
            return redirect(url_for("service_users_in_service",service_id = service_user.service_id))
        else:
            show_modal = True
            remaining_money = outstanding_money - cash_in

    return render_template("close_wallet_add_cash.html", service_user=service_user, last_wallet_id=last_wallet_id, outstanding_money=outstanding_money, show_modal=show_modal,remaining_money=remaining_money)
    #  if cash doesnt add up to total then propmpt to call manager or review reciepts
    

@app.route("/close_wallet_banking/<int:service_user_id>/<string:enter_seal>",methods=["GET","POST"])
@login_required(allowed_roles=["manager", "it","support"])
def close_wallet_banking(service_user_id,enter_seal):
    service_user = ServiceUser.query.get_or_404(service_user_id)
    last_wallet_entry = WalletEntry.query.filter_by(service_user_id=service_user_id).order_by(WalletEntry.id.desc()).first()
    last_entry_with_receipt = (
    WalletEntry.query
    .filter(WalletEntry.receipt_number != 0)
    .filter(WalletEntry.service_user_id == service_user_id)
    .order_by(WalletEntry.id.desc())
    .first())
    all_receipts = session.get('all_receipts', [])
    
    enter_seal = True if enter_seal.lower() == "true" else False

    print(enter_seal)
    if request.method == "POST":
        if last_entry_with_receipt is not None:
            receipt_number = last_entry_with_receipt.receipt_number + 1
        else:
            receipt_number = 1

        if enter_seal:
            new_seal_number = request.form.get("seal_number")
        else:
            new_seal_number = last_wallet_entry.seal_number

        wallet_entry = WalletEntry(
            service_user_id = service_user.id,
            staff_id = session["user"],
            date_time = datetime.now(),
            seal_number = new_seal_number,
            cash_amount = last_wallet_entry.cash_amount,
            bank_amount = last_wallet_entry.bank_amount - Decimal(request.form.get("bank_out")),
            cash_out = 0,
            cash_in = 0,
            bank_card_removed=bool(False),
            money_spent = Decimal(request.form.get("bank_out")),
            money_spent_description = request.form.get("money_spent_description"),
            bank_out = Decimal(request.form.get("bank_out")) ,
            bank_in = 0,
            receipt_number = receipt_number,
            is_cash_removed = False
            )
        db.session.add(wallet_entry)
        db.session.commit()
        receipt = [receipt_number, request.form.get("money_spent_description"), float(request.form.get("bank_out"))]
        all_receipts.append(receipt)

        # after first reciept added - bank card is put in and seal remains the same
        

         # Store updated receipts in session
        session['all_receipts'] = all_receipts
        return redirect(url_for("close_wallet_banking",service_user_id=service_user_id,enter_seal= "false"))
    else:
        return render_template("close_wallet_banking.html",service_user=service_user,all_receipts=all_receipts,enter_seal=enter_seal)


@app.route("/banking_into_wallet/<int:service_user_id>/<float:outstanding_money>",methods=["GET","POST"])
@login_required(allowed_roles=["manager", "it","support"])
def banking_into_wallet(service_user_id,outstanding_money):
    service_user = ServiceUser.query.get_or_404(service_user_id)
    last_wallet_entry = WalletEntry.query.filter_by(service_user_id=service_user_id).order_by(WalletEntry.id.desc()).first()
    last_entry_with_receipt = (
    WalletEntry.query
    .filter(WalletEntry.receipt_number != 0)
    .filter(WalletEntry.service_user_id == service_user_id)
    .order_by(WalletEntry.id.desc())
    .first())
    
    outstanding_money = Decimal(str(outstanding_money))

    if request.method == "POST":
        if last_entry_with_receipt is not None:
            receipt_number = last_entry_with_receipt.receipt_number + 1
        else:
            receipt_number = 1

        wallet_entry = WalletEntry(
            service_user_id = service_user.id,
            staff_id = session["user"],
            date_time = datetime.now(),
            seal_number = request.form.get("seal_number"),
            cash_amount = last_wallet_entry.cash_amount + Decimal(request.form.get("bank_out")),
            bank_amount = last_wallet_entry.bank_amount - Decimal(request.form.get("bank_out")),
            cash_out = Decimal(request.form.get("bank_out")),
            cash_in = 0,
            bank_card_removed=bool(False),
            money_spent = 0,
            money_spent_description = "Banking: Cash out of bank",
            bank_out = Decimal(request.form.get("bank_out")) ,
            bank_in = 0,
            receipt_number = receipt_number,
            is_cash_removed = True
            )
        db.session.add(wallet_entry)
        db.session.commit()

        last_wallet_entry = WalletEntry.query.filter_by(service_user_id=service_user_id).order_by(WalletEntry.id.desc()).first()
        new_outstanding_money = last_wallet_entry.cash_out + outstanding_money

        return redirect(url_for("close_wallet",service_user_id=service_user_id,last_wallet_id=last_wallet_entry.id,outstanding_money=new_outstanding_money))
    else:
        return render_template("banking_into_wallet.html",service_user=service_user,outstanding_money=outstanding_money)

@app.route("/set_up_wallet/<int:service_user_id>",methods=["GET","POST"])
@login_required(allowed_roles=["manager", "it","support"])
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
            receipt_number = 0,
            is_cash_removed = False
            )
        db.session.add(wallet_entry)
        db.session.commit()
        return redirect(url_for("service_users_in_service",service_id = service_user.service_id))
    else:
        return render_template("set_up_wallet.html",service_user=service_user)
            
@app.route("/check_seal/<int:service_user_id>", methods=["GET","POST"])
@login_required(allowed_roles=["manager", "it","support"])
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
@login_required(allowed_roles=["manager", "it","support"])
def view_wallet(service_user_id):
    wallet_entries = WalletEntry.query.filter_by(service_user_id=service_user_id).order_by(WalletEntry.id.desc()).all()
    staff = list(Staff.query.order_by(Staff.id).all())
    return render_template("view_wallet.html",wallet_entries=wallet_entries,staff=staff)

@app.route("/reconsile_in_or_out/<int:service_user_id>",methods=["GET","POST"]) 
@login_required(allowed_roles=["manager", "it","support"])
def reconsile_in_or_out(service_user_id):
    service_user = ServiceUser.query.get_or_404(service_user_id)
    if request.method == "POST":
        if request.form.get("in_or_out") == "bank_in":
            return redirect(url_for("reconsile_banking",service_user_id=service_user_id, bank_in = "True"))
        else:
            return redirect(url_for("reconsile_banking",service_user_id=service_user_id, bank_in = "False"))
    else:
        return render_template("reconsile_in_or_out.html",service_user=service_user)


@app.route("/reconsile_banking/<int:service_user_id>/<string:bank_in>",methods=["GET","POST"])
@login_required(allowed_roles=["manager", "it","support"])
def reconsile_banking(service_user_id,bank_in):
    service_user = ServiceUser.query.get_or_404(service_user_id)
    last_wallet_entry = WalletEntry.query.filter_by(service_user_id=service_user_id).order_by(WalletEntry.id.desc()).first()
    if request.method == "POST":
        if bank_in =="True":
            wallet_entry = WalletEntry(
                service_user_id = service_user.id,
                staff_id = session["user"],
                date_time = request.form.get("date")+ " 00:00:00.000000",
                seal_number = last_wallet_entry.seal_number,
                cash_amount = last_wallet_entry.cash_amount,
                bank_amount = last_wallet_entry.bank_amount + Decimal(request.form.get("bank_in")),
                cash_out = 0,
                cash_in = 0,
                bank_card_removed=bool(False),
                money_spent = 0,
                money_spent_description = "Reconsiliation: " + request.form.get("money_spent_description"),
                bank_out = 0 ,
                bank_in = Decimal(request.form.get("bank_in")),
                receipt_number = 0
                )
        else:
            wallet_entry = WalletEntry(
                service_user_id = service_user.id,
                staff_id = session["user"],
                date_time = request.form.get("date")+ " 00:00:00.000000",
                seal_number = last_wallet_entry.seal_number,
                cash_amount = last_wallet_entry.cash_amount,
                bank_amount = last_wallet_entry.bank_amount - Decimal(request.form.get("bank_out")),
                cash_out = 0,
                cash_in = 0,
                bank_card_removed=bool(False),
                money_spent = Decimal(request.form.get("bank_out")),
                money_spent_description = "Reconsiliation: " + request.form.get("money_spent_description"),
                bank_out = Decimal(request.form.get("bank_out")) ,
                bank_in = 0,
                receipt_number = 0
                )

        db.session.add(wallet_entry)
        db.session.commit()
        return redirect(url_for("reconsile_banking",service_user_id=service_user_id,bank_in=bank_in))
    else:
        return render_template("reconsile_banking.html",service_user=service_user,bank_in=bank_in)

