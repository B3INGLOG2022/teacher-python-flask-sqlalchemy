from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://toto:tata@db:3306/titi'
db = SQLAlchemy(app)

## Data model

class Student(db.Model,SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/students")
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students])
