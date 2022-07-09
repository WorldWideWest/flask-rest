from flask import Flask
from flask_restful import Resource, Api, marshal_with
from flask_sqlalchemy import SQLAlchemy

from models import Employee, db, RESOURCE_FIELDS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/Employee.db"
db.init_app(app)

api = Api(app)

class Employees(Resource):
    @marshal_with(RESOURCE_FIELDS)
    def get(self):
        return Employee.query.all()


api.add_resource(Employees, "/")

if __name__ == "__main__":
    app.run(debug = True)
