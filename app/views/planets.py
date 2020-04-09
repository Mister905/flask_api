from flask import Blueprint, jsonify
from ..models.Planet import Planet
from ..derp.PlanetSchema import planets_schema

planets = Blueprint("planets", __name__)


@planets.route("/planets", methods=["GET"])
def get_planets():
    try:
        planets = Planet.query.all()
        result = planets_schema.dump(planets)
        return jsonify(result)
    except Exception as err:
        return err
