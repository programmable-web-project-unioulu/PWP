import json
from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import Engine
from sqlalchemy import event
from django.db import IntegrityError
from werkzeug.exceptions import HTTPException
from sqlalchemy.ext.declarative import DeclarativeMeta

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class StorageItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qty = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    location = db.Column(db.String(64), nullable=False)

    product = db.relationship("Product", back_populates="in_storage")

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    handle = db.Column(db.String(64), unique=True, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)

    in_storage = db.relationship("StorageItem", back_populates="product")

class AlchemyEncoder(json.JSONEncoder):
    """ this class and function copied from https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json
        Is this in vain??? Can serialization be done differently"""

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

@app.route("/product/add/", methods=['POST'])
def add_product():
    """ Add Product via POST method"""
    try:
        prod_handle = request.json["handle"]
        product = Product.query.filter_by(handle=prod_handle).first()
        if product == None:
            handle = str(request.json["handle"])
            weight = float(request.json["weight"])
            price = float(request.json["price"])
            prod = Product(
                handle=handle,
                weight=weight,
                price=price
            )
            db.session.add(prod)
            db.session.commit()
            return "PASS",201
        else:
            return "Handle already exists", 409
    except (KeyError,ValueError, IntegrityError):
        return "Weight and price must be numbers", 400

@app.route("/storage/<product>/add/", methods=['POST'])
def add_to_storage(product):
    """ Adds product to the storage - creates link between Product and Storage item"""
    try:
        product = Product.query.filter_by(handle=product).first()
        if product:
            location = str(request.json["location"])
            qty = int(request.json["qty"])
            storage_item = StorageItem(
                location=location,
                qty=qty,
                product_id=product.id
            )
            """ Some relationship forcing here? """
            #product = db.relationship("Product",backref=) #TODO
            product.in_storage.append(storage_item)
            db.session.add(product)
            db.session.add(storage_item)
            db.session.commit()
            return "PASS",201
        else:
            return "Product not found", 409
    except (KeyError,ValueError, IntegrityError):
        return "Qty must be and integer", 400

@app.route("/storage/", methods=['GET'])
def get_inventory():
    """ Creates JSON format output from storaged items -
        Does this require AlchemyEncoder class or not? What is the best way to print data out in JSON format"""
    try:
        storage = Product.query.all()
        for product in storage:
            #product_as_json = json.dumps(product,cls=AlchemyEncoder)
            #print(product_as_json)
            print(product.handle)
            print(product.weight)
            print(product.price)
            product_id = product.id
            inventory = StorageItem.query.all()
            for item in inventory:
                #print(item.product_id)
                if item.product_id == product_id:
                    print(f"location:{item.location}")
                    print(f"qty: {item.qty}")
        return "PASS",201
    except (KeyError,ValueError, IntegrityError):
        return "Qty must be and integer", 400

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    if e.code == 405:
        response = "POST method required", e.code
    if e.code == 415:
        response = "Request content must be JSON", e.code
    return response

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

db.create_all()
