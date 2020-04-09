from flask_marshmallow import Marshmallow

ma = Marshmallow()


class PlanetSchema(ma.Schema):
    class Meta:
        fields = (
            "planet_id",
            "planet_name",
            "planet_type",
            "home_star",
            "mass",
            "radius",
            "distance",
        )


planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)
