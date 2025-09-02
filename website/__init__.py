from flask import Flask
from dotenv import load_dotenv
from .views import main_blueprint

load_dotenv()

def create_app():

    app = Flask(__name__)
    app.register_blueprint(main_blueprint)

    return app

if __name__ == '__main__':
    create_app()