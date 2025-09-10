'''
init.py - audrey palmer

defines how the app is set up and lists names of necessary keys to run the app
initializes login manager with flask with some function definitions
registers blueprints for page viewing and initializes the database
'''


import os

from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv

from .database import db
from .models import User
from .functional_pages import fp, login
from .blueprint_pages import bp

load_dotenv()

def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        os.environ.get("JAWSDB_URL")
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    db.init_app(app)

    # for flask login
    login_manager = LoginManager(app)
    login_manager.login_view = "fp.login"

    @login_manager.user_loader
    def load_user(user_id) :
        # return User.query.get(int(user_id))
        return User.query.get(user_id)

    
    app.register_blueprint(bp)
    app.register_blueprint(fp)

    with app.app_context() :
        db.create_all()

    return app