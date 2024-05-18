from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import routes
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    # Creating new App
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Simple Secret Key"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Adding the database to the application
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    # Adding routes
    app.register_blueprint(routes, url_prefix="/")

    # Creating the database
    create_database(app)

    return app


def create_database(app):
    # If the database does not exist, create it
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Database Created!")
