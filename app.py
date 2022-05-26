from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://toto:tata@db:3306/titi'
db = SQLAlchemy(app)

## Data model

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=True, nullable=False)
    lastname = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
