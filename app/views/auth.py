from flask import Blueprint, jsonify, request
from ..models.User import User
from ..extensions.sqlalchemy import db
from ..extensions.flask_mail import mail
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_mail import Message

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["POST"])
def register():
    try:
        email = request.json["email"]
        prexisting_email = User.query.filter_by(email=email).first()
        if prexisting_email:
            return jsonify(message="A user with that email already exists"), 409
        first_name = request.json["first_name"]
        last_name = request.json["last_name"]
        password = request.json["password"]
        new_user = User(
            first_name=first_name, last_name=last_name, email=email, password=password
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify(message="User creation successful")

    except Exception as err:
        return err


@auth.route("/login", methods=["POST"])
def login():
    try:
        email = request.json["email"]
        password = request.json["password"]
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            access_token = create_access_token(identity=email)
            return jsonify(message="authenticated", access_token=access_token)
        else:
            return jsonify(message="Login failed"), 401
    except Exception as err:
        return err


@auth.route("/retrieve-password/<string:email>", methods=["GET"])
def retrieve_password(email: str):
    try:
        user = User.query.filter_by(email=email).first()
        if user:
            message = Message(
                "Your password is " + user.password,
                sender="support@acme.com",
                recipients=[email],
            )
            mail.send(message)
            return jsonify(message="Password sent to " + email)
        else:
            return jsonify(message="No account with that email"), 401
    except Exception as err:
        return err
