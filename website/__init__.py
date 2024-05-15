from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME =  "database.db"


def create_app():
    #Creating new App
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Simple Secret Key"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Adding routes
    from .routes import routes
    app.register_blueprint(routes, url_prefix="/")




        return app

    return app
