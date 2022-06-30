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

# ============================================================
import flask_login

""" app.py: - the main flask server """
# ============================================================

from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


"""General Config"""
db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
login_manager = LoginManager(app)

# DB ORM
migrate = Migrate()
db.init_app(app)
if app.config["SQLALCHEMY_DATABASE_URI"].startswith("mysql"):
    migrate.init_app(app, db, render_as_batch=True)
else:
    migrate.init_app(app, db)

''''
  =====================================
            Login Manager
  ====================================
'''


class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    pass


@login_manager.request_loader
def request_loader(request):
    pass


@login_manager.unauthorized_handler
def unauthorized_handler():
    return '404'


''' ERROR HANDLERS '''


def page_not_found(e):
    return render_template("error_pages/404.html"), 404


def internal_server_error(e):
    return render_template("error_pages/500.html"), 500

#  Register Error Handlers


app.register_error_handler(404, page_not_found)

app.register_error_handler(500, internal_server_error)



"""
  =====================================
            Blueprint routes
 ======================================     
"""

# import the views

from views.main_page import index_views

"""Register Blueprints"""
# Index Page - /
app.register_blueprint(index_views.bp)


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host="0.0.0.0", port=8080)


