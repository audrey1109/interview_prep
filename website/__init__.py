import os

from flask import Flask
from dotenv import load_dotenv

from .database import db
from .views import main_blueprint

load_dotenv()

def create_app():

    app = Flask(__name__)
    app.register_blueprint(main_blueprint)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        os.environ.get("DATABASE_URL")
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context() :
        db.create_all()

    return app