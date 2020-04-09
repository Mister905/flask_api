from flask import Blueprint, jsonify, request
from ..models.User import User
from ..extensions.sqlalchemy import db

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
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(message="User creation successful")
        
    except Exception as err:
        return err


@auth.route("/login", methods=["POST"])
def test():
    try:
        # planets = Planet.query.all()
        # result = planets_schema.dump(planets)
        # return jsonify(result)
        return "DEfdsa"
    except Exception as err:
        return err
