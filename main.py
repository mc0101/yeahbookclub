from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from hashutils import make_pw_hash, check_pw_hash

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://yeah-book-club:yeahbookclub@localhost:8889/yeah-book-club'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'abcdefg'

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    emailaddress = db.Column(db.String(120), unique=True)
    pw_hash = db.Column(db.String(120))
    location = db.Column(db.String, db.ForeignKey("location.id"))
    clubs = db.relationship("Club", backref="member")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.pw_hash = make_pw_has(password)


