from flask import Blueprint
from ..extensions.sqlalchemy import db
from ..models.Planet import Planet
from ..models.User import User

scripts = Blueprint("scripts", __name__)


@scripts.cli.command("script_test")
def script_test():
    print("script_test!")


@scripts.cli.command("db_create")
def db_create():
    db.create_all()
    print("Database created!")


@scripts.cli.command("db_drop")
def db_drop():
    db.drop_all()
    print("Database dropped!")


@scripts.cli.command("db_seed")
def db_seed():
    mercury = Planet(
        planet_name="Mercury",
        planet_type="Class D",
        home_star="Sol",
        mass=2.258e23,
        radius=1516,
        distance=35.98e6,
    )

    venus = Planet(
        planet_name="Venus",
        planet_type="Class K",
        home_star="Sol",
        mass=4.867e24,
        radius=3760,
        distance=67.24e6,
    )

    earth = Planet(
        planet_name="Earth",
        planet_type="Class M",
        home_star="Sol",
        mass=5.972e24,
        radius=3959,
        distance=92.96e6,
    )

    db.session.add(mercury)
    db.session.add(venus)
    db.session.add(earth)

    test_user = User(
        first_name="John",
        last_name="Doe",
        email="jdoe@gmail.com",
        password="jdoe@gmail.com",
    )

    db.session.add(test_user)
    db.session.commit()
    print("Database seeded!")
