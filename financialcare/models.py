from financialcare import db


user_service =db.Table("user_service",
db.Column("user_id",db.Integer,db.ForeignKey("user.id"),primary_key=True),
db.Column("service_id",db.Integer,db.ForeignKey("service.id"),primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),nullable =False)
    access =db.Column(db.String)
    services =db.relationship("Service",secondary= user_service,backref ="users")

    def __repr__(self):
        return f"<user: {self.name}>"



class Service(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),nullable =False)
    def __repr__(self):
        return f"<service: {self.name}>"