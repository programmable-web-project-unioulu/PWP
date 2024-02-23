from werkzeug.routing import BaseConverter
from werkzeug.exceptions import NotFound

from inventorymanager.constants import *
from inventorymanager.models import *

class WarehouseConverter(BaseConverter):
    
    def to_python(self, warehouse_id):
        warehouse = Warehouse.query.filter_by(warehouse_id=warehouse_id).first()
        if warehouse is None:
            raise NotFound
        return warehouse
        
    def to_url(self, warehouse):
        return warehouse.warehouse_id
    

class ItemConverter(BaseConverter):
    
    def to_python(self, name):
        item = Item.query.filter_by(name=name).first()
        if item is None:
            raise NotFound
        return item