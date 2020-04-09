from flask import Blueprint, jsonify, request
from ..models.Planet import Planet
from ..marshmallow_schema.PlanetSchema import planets_schema, planet_schema
from ..extensions.sqlalchemy import db
from flask_jwt_extended import jwt_required

planets = Blueprint("planets", __name__)

# Get Planets
@planets.route("/planets", methods=["GET"])
def get_planets():
    try:
        planets = Planet.query.all()
        result = planets_schema.dump(planets)
        return jsonify(result)
    except Exception as err:
        return err


# Get Planet by ID
@planets.route("/planets/<int:planet_id>", methods=["GET"])
def get_planet_by_id(planet_id):
    try:
        planet = Planet.query.filter_by(planet_id=planet_id).first()
        if planet:
            result = planet_schema.dump(planet)
            return jsonify(result)
        else:
            return jsonify(message="Planet not found"), 404
    except Exception as err:
        return err


# Create Planet
@planets.route("/planets", methods=["POST"])
@jwt_required
def create_planet():
    try:
        planet_name = request.json["planet_name"]
        planet_type = request.json["planet_type"]
        home_star = request.json["home_star"]
        mass = float(request.json["mass"])
        radius = float(request.json["radius"])
        distance = float(request.json["distance"])
        new_planet = Planet(
            planet_name=planet_name,
            planet_type=planet_type,
            home_star=home_star,
            mass=mass,
            radius=radius,
            distance=distance,
        )
        db.session.add(new_planet)
        db.session.commit()
        return jsonify(message="Planet creation successful"), 201
    except Exception as err:
        return err


# Update Planet
@planets.route("/planets", methods=["PUT"])
@jwt_required
def update_planet():
    try:
        planet_id = int(request.json["planet_id"])
        planet = Planet.query.filter_by(planet_id=planet_id).first()
        if planet:
            planet.planet_name = request.json["planet_name"]
            planet.planet_type = request.json["planet_type"]
            planet.home_star = request.json["home_star"]
            planet.mass = float(request.json["mass"])
            planet.radius = float(request.json["radius"])
            planet.distance = float(request.json["distance"])
            db.session.commit()
            return jsonify(message="Planet update successful"), 202
    except Exception as err:
        return err


# Delete Planet
@planets.route("/planets/<int:planet_id>", methods=["DELETE"])
@jwt_required
def delete_planet(planet_id: int):
    try:
        planet = Planet.query.filter_by(planet_id=planet_id).first()
        if planet:
            db.session.delete(planet)
            db.session.commit()
            return jsonify(message="You deleted a planet"), 202
        else:
            return jsonify(message="Couldn't find planet")
    except Exception as err:
        return err
