# /usr/bin/python
# Copyright 2022 Jeremy Stevens <jeremiahstevens@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
__version__ = '0.0.1'  # current version
__author__ = 'Jeremy Stevens'  # author
__revision__ = '1'  # revision

# ============================================================
import time

from sqlalchemy import create_engine
import flask
import flask_login
from werkzeug.security import check_password_hash, generate_password_hash

""" index_views.py - main index page """
# ============================================================

from flask import Blueprint, url_for, redirect, current_app, session, render_template, request, flash
# import users from models
from models.users import Users, db
from werkzeug.security import check_password_hash, generate_password_hash
# use SQLALCHEMY_DATABASE_URI to connect to the database
from config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

bp = Blueprint("index_views", __name__, url_prefix="/")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["email"]
        password = request.form["password"]
        user = Users.query.filter_by(email=username).first()
        if user:
            if check_password_hash(user.password, password):
                session["user_id"] = user.id
                print(session["user_id"])
                return redirect(url_for("index_views.index"))
            else:
                flash("Incorrect username or password")
        else:
            flash("User not found")
    return render_template("main_page/index.html")


#  index and login page
@bp.route("/", methods=["GET", "POST"])
def index():
    # if user is already logged in
    if "user_id" in session:
        return redirect(url_for("main_page.main_page"))
    return render_template("main_page/index.html")


# register new account
@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template("main_page/index.html")
        # get form data
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        email = request.form['email']
        # check if email is already in use
        if Users.query.filter_by(email=email).first():
            flash("Email already in use, please use another email")
            return redirect(url_for("index_views.register"))
        # create new user in Users
        users = Users()
        db.session.add(Users(password=password, email=email))
        db.session.commit()
        flash("Account created, you can now login")
        # redirect to login page after registration
        return redirect(url_for("index_views.index"))
