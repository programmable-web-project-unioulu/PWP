import json
from jsonschema import validate, ValidationError
from flask import Response, abort, request, url_for
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from inventorymanager.models import Item
from inventorymanager import db
from inventorymanager.constants import *


class ItemCollection(Resource):
    
    def post(self):
        if not request.json:
            abort(415, "Unsupported media type")

        try:
            validate(request.json, Item.get_schema())
            item = Item()
            item.deserialize(request.json)
        
            db.session.add(item)
            db.session.commit()

        except ValidationError as e:
            return abort(400, e.message)

        except IntegrityError:
            return abort(409, "Item already exists")

        return Response(status=201, headers={
            "Location": url_for("api.itemitem", item=item)
        })
    



class ItemItem(Resource):
    
    def get(self, item):
        pass
    
