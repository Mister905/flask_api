from flask import Flask
from .extensions.sqlalchemy import db
from .extensions.flask_mail import mail
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_mail import Mail, Message

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
    app.config["JWT_SECRET_KEY"] = "mr$LMk7UTjkc"
    app.config['MAIL_SERVER']='smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 2525
    app.config['MAIL_USERNAME'] = 'd4643680d3cf6b'
    app.config['MAIL_PASSWORD'] = '5ed2d9bb46c00d'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    db.init_app(app)
    mail.init_app(app)
    ma = Marshmallow(app)
    jwt = JWTManager(app)
    # Blueprints
    app.register_blueprint(test)
    app.register_blueprint(scripts)
    app.register_blueprint(planets)
    app.register_blueprint(auth)
    return app
