import bcrypt
from financialcare import db



staff_service =db.Table("staff_service",
db.Column("staff_id",db.Integer,db.ForeignKey("staff.id"),primary_key=True),
db.Column("service_id",db.Integer,db.ForeignKey("service.id"),primary_key=True)
)

class Staff(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),nullable =False)
    email =db.Column(db.String(128),nullable =False)
    password =db.Column(db.String(128),nullable =False)
    access =db.Column(db.String,nullable =False)
    services =db.relationship("Service",secondary= staff_service,backref ="staff")

    def __repr__(self):
        return f"<staff: {self.name}>"

    def set_password(self, plain_text_password):
        self.password = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, plain_text_password):
        return bcrypt.checkpw(plain_text_password.encode('utf-8'), self.password.encode('utf-8'))



class Service(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),nullable =False)
    service_user=db.relationship("ServiceUser",backref="service")
    def __repr__(self):
        return f"<service: {self.name}>"


class ServiceUser(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),nullable=False)
    bank = db.Column(db.String(128),nullable=False)
    service_id =db.Column(db.Integer,db.ForeignKey("service.id"),nullable=False)
    

class WalletEntry(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    service_user_id = db.Column(db.Integer,db.ForeignKey("service_user.id"),nullable=False)
    staff_id = db.Column(db.Integer,db.ForeignKey("staff.id"),nullable=False)
    date_time = db.Column(db.DateTime,nullable=False)
    seal_number = db.Column(db.Integer,nullable=False)
    cash_amount = db.Column(db.Numeric(precision=10, scale=2),nullable=False)
    bank_amount = db.Column(db.Numeric(precision=10, scale=2),nullable=False)
    cash_out = db.Column(db.Numeric(precision=10, scale=2))
    cash_in = db.Column(db.Numeric(precision=10, scale=2))
    bank_card_removed = db.Column(db.Boolean,default=False,nullable=False)
    money_spent = db.Column(db.Numeric(precision=10, scale=2))
    money_spent_description = db.Column(db.String)
    bank_out = db.Column(db.Numeric(precision=10, scale=2))
    bank_in = db.Column(db.Numeric(precision=10, scale=2))
    receipt_number =db.Column(db.Integer)
    
    staff = db.relationship('Staff', backref='wallet_entries')

    