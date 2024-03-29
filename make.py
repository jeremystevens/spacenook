import flask
from flask import Flask, render_template, request, url_for, redirect, flash, session, send_file, Response, abort
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, DateTime, create_engine
from sqlalchemy.sql import func

app = Flask(__name__)
app.secret_key = '7139abd5380e6aa76084caf01740e1f4a4d96b9fcc9e27b36017dccbcdd80c10'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://smadmin:123@localhost/socialmedia"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_PERMANENT"] = False
app.config['SESSION_TYPE'] = 'filesystem'

db = SQLAlchemy(app)

#engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)

# PyMySQL
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    db.create_all()
    return app


class Users(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)  # is active
    is_active = db.Column(db.Boolean, default=False)
    is_reported = db.Column(db.Boolean, default=False)
    is_blocked = db.Column(db.Boolean, default=False)
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(DateTime(timezone=True), onupdate=func.now())


class Profile(db.Model):
    userProfileID = db.Column(db.Integer, autoincrement=True, primary_key=True)
    userID = db.Column(db.Integer, nullable=False)
    firstName = db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    locationID = db.Column(db.Integer, nullable=True)
    # gender charset
    gender = db.Column(db.String(50), nullable=True)
    # date of birth Column
    dob = db.Column(db.String(200), nullable=True)
    occupation = db.Column(db.String(200), nullable=True)
    about = db.Column(db.Text(6400), nullable=True)
    dateUpdated = db.Column(DateTime(timezone=True), server_default=func.now())


class Locations(db.Model):
    locationID = db.Column(db.Integer, autoincrement=True, primary_key=True)
    City = db.Column(db.String(80), nullable=False)
    State = db.Column(db.String(80), nullable=False)
    zipcode = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(80), nullable=False)