from flask_sqlalchemy import SQLAlchemy
from flask_restful import fields

db = SQLAlchemy()

RESOURCE_FIELDS = {
    "id": fields.Integer,
    "first_name": fields.String,
    "last_name": fields.String,
    "email": fields.String,
}

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(150), nullable = False, unique = True)

    def __repr__(self):
        return f"{ self.first_name } { self.last_name }: { self.email }"


