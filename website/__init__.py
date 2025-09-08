import os

from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv

from .database import db
from .models import User
from .page_functions import pf, login
from .views import main_blueprint

load_dotenv()

def create_app():

    app = Flask(__name__)
    # app.register_blueprint(main_blueprint)
    # app.register_blueprint(page_functions)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        os.environ.get("JAWSDB_URL")
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # for logins
    lm = LoginManager()
    lm.login_view = "pf.login"
    lm.init_app(app)

    @lm.user_loader
    def load_user(user_id) :
        return User.query.get(int(user_id))
    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(pf)

    with app.app_context() :
        db.create_all()

    return app