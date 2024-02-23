from werkzeug.routing import BaseConverter
from werkzeug.exceptions import NotFound
import json
from flask import url_for, request, Response

from inventorymanager.constants import *
from inventorymanager.models import *

class WarehouseConverter(BaseConverter):
    
    def to_python(self, value):
        warehouse = Warehouse.query.filter_by(warehouse_id=value).first()
        if warehouse is None:
            raise NotFound
        return warehouse
        
    def to_url(self, value):
        return value.warehouse_id
    

class ItemConverter(BaseConverter):
    
    def to_python(self, value):
        item = Item.query.filter_by(name=value).first()
        if item is None:
            raise NotFound
        return item
    
    def to_url(self, value):
        return value.name
    

# def create_error_response(status_code, title, message=None):
#     """
#     Utility function that creates a Mason error response
#     :param status_code: integer that represents a valid HTTP status code
#     :param title: The title of the error (e.g. `Bad Request', 'Conflict')
#     :param message: Longer message explaining what caused the error
#     :return: A populated Response object
#     """
#     resource_url = request.path
#     body = MasonBuilder(resource_url=resource_url)
#     body.add_error(title, message)
#     body.add_control("profile", href=ERROR_PROFILE)
#     return Response(json.dumps(body), status_code, mimetype=MASON)