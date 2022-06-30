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

# ============================================================
import flask

""" index_views.py - main index page """
# ============================================================

from flask import Blueprint, url_for, redirect, current_app, session, render_template
# import users from models
from models.users import Users
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint("index_views", __name__, url_prefix="/")

#  index and login page
@bp.route("/", methods=["GET", "POST"])
def index():
    # if user is already logged in
    if "user_id" in session:
        pass
        #return redirect(url_for("main_page.main_page"))
    # if login form is submitted
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']
    # if GET request show login form
    return render_template("main_page/index.html")


# register new account
@bp.route("/register", methods=["GET", "POST"])
def register():
    if flask.request.method == 'POST':
        # get form data
        firstname = flask.request.form['inputFirstName']
        lastname = flask.request.form['inputLastName']
        email = flask.request.form['inputEmail']
        username = flask.request.form['inputUsername']
        password = flask.request.form['inputPassword']
        # create new user
        new_user = Users(firstname, lastname, email, username, password)
        # add user to database
        new_user.add_user()
        # redirect to login page
        return redirect(url_for("index_views.index"))
        pass
    # if GET request show register form
    return render_template("main_page/register.html")

