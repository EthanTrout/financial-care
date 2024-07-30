import bcrypt
from financialcare import db



user_service =db.Table("user_service",
db.Column("user_id",db.Integer,db.ForeignKey("user.id"),primary_key=True),
db.Column("service_id",db.Integer,db.ForeignKey("service.id"),primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),nullable =False)
    email =db.Column(db.String(128),nullable =False)
    password =db.Column(db.String(128),nullable =False)
    access =db.Column(db.String,nullable =False)
    services =db.relationship("Service",secondary= user_service,backref ="users")

    def __repr__(self):
        return f"<user: {self.name}>"

    def set_password(self, plain_text_password):
        self.password = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, plain_text_password):
        return bcrypt.checkpw(plain_text_password.encode('utf-8'), self.password.encode('utf-8'))



class Service(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),nullable =False)
    def __repr__(self):
        return f"<service: {self.name}>"