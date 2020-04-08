from flask import Flask
from .extensions.sqlalchemy import db
from .views.test import test


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:r0W[qJnK@localhost:3306/flask_rest_api'

    db.init_app(app)

    app.register_blueprint(test)

    return app
