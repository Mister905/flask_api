from flask import Flask
from .extensions.sqlalchemy import db
from flask_marshmallow import Marshmallow

# Views
from .views.test import test
from .views.planets import planets
from .views.auth import auth

# Scripts
from .scripts.index import scripts


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql://admin:r0W[qJnK@localhost:3306/flask_api"
    db.init_app(app)
    ma = Marshmallow(app)
    # Blueprints
    app.register_blueprint(test)
    app.register_blueprint(scripts)
    app.register_blueprint(planets)
    app.register_blueprint(auth)
    return app
