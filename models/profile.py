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
# ============================================================
#    profile Model Version 0.0.1
# ============================================================

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, DateTime, func

db = SQLAlchemy()


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