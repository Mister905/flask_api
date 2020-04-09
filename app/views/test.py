from flask import Blueprint, jsonify
from sqlalchemy import text
from ..extensions.sqlalchemy import db

test = Blueprint("test", __name__)


@test.route("/")
def testdb():
    try:
        db.session.query("1").from_statement(text("SELECT 1")).all()
        return "<h1>It works.</h1>"
    except Exception as err:

        return err


@test.route("/not_found")
def not_found():
    return jsonify(message="404 Error - Resource Not Found"), 404


@test.route("/url_params/<string:name>/<int:age>")
def url_params(name: str, age: int):
    if age < 18:
        return jsonify(message="Sorry " + name + ", you are not old enough!"), 401
    else:
        return jsonify(message="Welcome " + name + "!")
