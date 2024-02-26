import json
from jsonschema import validate, ValidationError
from flask import Response, abort, request, url_for
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from inventorymanager.models import Item
from inventorymanager import db
from inventorymanager.constants import *


class ItemCollection(Resource):
    

    def get(self):
        body = []
        for item in Item.query.all():
            item_json = item.serialize()
            item_json["uri"] = url_for("api.itemitem", item=item)
            body.append(item_json)

        return Response(json.dumps(body), 200)


    def post(self):
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
    
