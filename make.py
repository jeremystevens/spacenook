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
    # username db
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)  # is active
    is_active = db.Column(db.Boolean, default=False)
    is_reported = db.Column(db.Boolean, default=False)
    is_blocked = db.Column(db.Boolean, default=False)
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(DateTime(timezone=True), onupdate=func.now())