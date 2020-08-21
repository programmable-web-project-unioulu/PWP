import click
from flask.cli import with_appcontext
from . import db


class Plant(db.Model):
    """
    Plant table
    acquired: DateTime (optional)
    specie:   String
    location: String (optional)
    name:     String(64) (unique)
    """

    uuid = db.Column(db.Integer, primary_key=True)
    #acquired = db.Column(db.DateTime, nullable=True)
    specie = db.Column(db.String(128), nullable=False)
    #location = db.Column(db.String(128), nullable=True)
    name = db.Column(db.String(64), nullable=False, unique=True)


    @staticmethod
    def get_schema():
        """Returns schema for Plant"""
        schema = {
                "type": "object",
                "required": ["specie", "name"]
                }
        props = schema["properties"] = {}
        props["specie"] = {
                "description": "Specie of the plant",
                "type": "string"
                }
        props["name"] = {
                "description": "Name of the plant",
                "type": "string"
                }
        return schema



class PlantGeneral(db.Model):
    """
    PlantGeneral table
    water:       String (optional)
    humidity:    String (optional)
    temperature: String (optional)
    soil:        String (optional)
    instructions String
    specie       String
    """
    uuid = db.Column(db.Integer, primary_key=True)
    water = db.Column(db.String(64), nullable=True)
    humidity = db.Column(db.String(64), nullable=True)
    temperature = db.Column(db.String(64), nullable=True)
    soil = db.Column(db.String(64), nullable=True)
    instruction = db.Column(db.String(512), nullable=False)
    specie = db.Column(db.String(128), nullable=False)


    @staticmethod
    def get_schema():
        """ Returns the schema for PlantGeneral"""
        schema = {
                "type": "object",
                "required": ["instructions", "specie"]
                }
        props = schema["properties"] = {}
        props["instructions"] = {
                "description": "Instructions how to take care of the plant",
                "type": "string"
                }
        props["specie"] = {
                "description": "Specie of the plant",
                "type": "string"
                }
        return schema


class Diary(db.Model):
    """
    Diary database
    date:       DateTime
    water_info; String (optional)
    wellbeing:  String (optional)
    description String
    """
    uuid = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    water_info = db.Column(db.String, nullable=True)
    wellbeing = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=False)

    @staticmethod
    def get_schema():
        """ Returns the schema for Diary"""
        schema = {
                "type": "object",
                "required": ["date", "description"]
                }
        props = schema["properties"] = {}
        props["date"] = {
                "description": "Date of the diary record",
                "type": "string"
                }
        props["description"] = {
                "description": "The journal itself",
                "type": "string"
                }

@click.command("init-db")
@with_appcontext
def init_db_command():
    db.create_all()
