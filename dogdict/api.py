import os
from sqlalchemy.engine import Engine
from sqlalchemy import event
from flask_restful import Api
from flask import Blueprint

from dogdict.resources.breed import BreedCollection, BreedItem
from dogdict.resources.group import GroupCollection, GroupItem
from dogdict.resources.fact import FactCollection, FactItem
from dogdict.resources.characteristic import CharacteristicCollection

"""
Config is copied from exercises
"""

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

api_bp = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_bp)

api.add_resource(GroupCollection, "/groups/")
api.add_resource(BreedCollection, "/breeds/")
api.add_resource(FactCollection, "/facts/")
api.add_resource(CharacteristicCollection, "/characteristics/")

api.add_resource(GroupItem, "/groups/<group:group>/")
api.add_resource(BreedItem, "/breeds/<breed:breed>/")
api.add_resource(FactItem, "/facts/<fact:fact>/")
