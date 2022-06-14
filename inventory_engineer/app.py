import json
from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import Engine
from sqlalchemy import event
from django.db import IntegrityError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.Integer, db.ForeignKey("sensor.id"))
    value = db.Column(db.Float, nullable=False)
    time = db.Column(db.DateTime, nullable=False)

    sensor = db.relationship("Sensor", back_populates="measurements")


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


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, unique=True)
    model = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(128), nullable=False)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)

    measurements = db.relationship("Measurement", cascade="all, delete-orphan", back_populates="sensor")

data = {"handle":"Handleri", "weight": 33.3, "price":3.33}

@app.route("/product/add/", methods=['POST'])
def add_product():
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
    try:
        prod_handle = str(product)
        print(prod_handle)
        product = Product.query.filter_by(handle=prod_handle).first()
        print(product)
        if product:
            location = str(request.json["location"])
            qty = int(request.json["qty"])
            product.append() #TODO inventory
            Inventory = Product(
                location=location,
                qty=qty
            )
            db.session.add(prod)
            db.session.commit()
            return "PASS",201
        else:
            return "Product not found", 409
    except (KeyError,ValueError, IntegrityError):
        return "Qty must be and integer", 400

@app.route("/storage/", methods=['GET'])
def get_inventory():
    try:
        storage = Product.query.all()
        print(storage)
        for product in storage:
            print(product.handle)
            print(product.weight)
            print(product.price)
            print("")
        return "PASS",201
    except (KeyError,ValueError, IntegrityError):
        return "Qty must be and integer", 400

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()



db.create_all()
