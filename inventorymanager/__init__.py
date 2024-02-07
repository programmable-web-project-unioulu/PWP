from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from inventorymanager.config import Config

db = SQLAlchemy()

def create_app(config_Class=Config):
    app = Flask(__name__)
    app.config.from_object(config_Class)
    db.init_app(app)

    # Import All Models
    from inventorymanager.models import Location, Warehouse, Item, Stock, Catalogue

    # Assuming the CLI commands are defined in the models.py or another module,
    # import them here to register with the app
    from inventorymanager.models import init_db_command, create_dummy_data

    app.cli.add_command(init_db_command)
    app.cli.add_command(create_dummy_data)

    return app
