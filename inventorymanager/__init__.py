from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from inventorymanager.config import Config

db = SQLAlchemy()

# Structure learned from the following sources:
# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/
# https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy#the-target-application-structure
# https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application#step-2-setting-up-the-database-and-model
def create_app(config_Class=Config):
    app = Flask(__name__)
    app.config.from_object(config_Class)
    db.init_app(app)

    # Import All Models (not sure why yet, its a thing-to-do to make this work)
    from inventorymanager.models import Location, Warehouse, Item, Stock, Catalogue

    # CLI commands to populate db
    from inventorymanager.models import init_db_command, create_dummy_data

    app.cli.add_command(init_db_command)
    app.cli.add_command(create_dummy_data)

    return app
