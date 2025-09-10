'''
models.py - audrey palmer

definies the models used in my website's database
'''

from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

from .database import db

# models -----------------------------------------------------------------------

class User(db.Model, UserMixin) :
    '''
    if people want to log in or i need something to associate them with
    '''
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(30), unique = True, nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    password_hash = db.Column(db.String(256), nullable = False)

    verified = db.Column(db.Boolean, default = False, nullable = False)
    admin_status = db.Column(db.Boolean, default = False, nullable = False)
    date_creation = db.Column(db.DateTime(timezone = True), default=func.now())

    start_session = db.Column(db.DateTime(timezone = True), nullable = True)
    end_session = db.Column(db.DateTime(timezone = True), nullable = True)

    # # relationship definitions
    # visits= db.relationship("UserPageVisits", back_populates = "user")

    # internal functions
    def set_password(self, password) :
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) :
        return check_password_hash(self.password_hash, password)


class Page(db.Model) :
    '''
    stores metrics data (hopefully)
    '''
    table_name = "page"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    page_name = db.Column(db.String(20), unique  = True, nullable = False)

    views = db.Column(db.Integer, default = 0)
    total_users = db.Column(db.Integer, default = 0)
    # conversion_rate = db.Column(db.Float, default = 100)
    # signups = db.Column(db.Integer, default = 0)

    # # relationship definitions
    # visits = db.relationship("UserPageVisits", back_populates = "page")


class Visit(db.Model) :
    '''
    stores visit data for metrics, time focused
    '''
    table_name = "visit"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    start_time = db.Column(db.DateTime, nullable = False)
    end_time = db.Column(db.DateTime, nullable = False)
    duration = db.Column(db.Float, nullable = False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    
    # relationship definitions
    user = db.relationship("User", backref = "visits")

# # relationships ------------------------------------------------------------------

# class UserPageVisits(db.Model) :
#     '''
#     for each user, contains a boolean representing what pages they've visited
#     '''


