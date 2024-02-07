# First, we'll import the necessary libraries: Flask and Flask_SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
# Set the SQLAlchemy Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask application
db = SQLAlchemy(app)

# Association table for a many-to-many relationship between Items and Warehouses
# From https://lovelace.oulu.fi/ohjelmoitava-web/ohjelmoitava-web/introduction-to-web-development/#structure-of-databases
items_warehouses_association = db.Table('items_warehouses',
    db.Column('item_id', db.Integer, db.ForeignKey('item.id'), primary_key=True),
    db.Column('warehouse_id', db.Integer, db.ForeignKey('warehouse.id'), primary_key=True)
)

# Location model
class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    country = db.Column(db.String(64), nullable=False, default="Finland")
    postal_code = db.Column(db.String(8), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    street_name = db.Column(db.String(64), nullable=False)
    house_number = db.Column(db.Integer, nullable=True)

# Warehouse model
class Warehouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    manager = db.Column(db.String(64), nullable=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id', ondelete='CASCADE'), nullable=True)
    location = db.relationship('Location', backref=db.backref('warehouses', lazy=True))

    # Many-to-many relationship with Items
    items = db.relationship('Item', secondary=items_warehouses_association, back_populates="warehouses")

# Item model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    category = db.Column(db.String(64), nullable=True)
    weight = db.Column(db.Float, nullable=True)

    # Many-to-many relationship with Warehouses
    warehouses = db.relationship('Warehouse', secondary=items_warehouses_association, back_populates="items")


# Stock model
class Stock(db.Model):
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouse.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    shelf_price = db.Column(db.Float, nullable=True)

    # Relationship
    item = db.relationship('Item', backref=db.backref('stocks', lazy=True))
    warehouse = db.relationship('Warehouse', backref=db.backref('stocks', lazy=True))

# Catalogue model
class Catalogue(db.Model):
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    supplier_name = db.Column(db.String(64), primary_key=True)
    min_order = db.Column(db.Integer, nullable=False)
    order_price = db.Column(db.Float, nullable=True)

    # Relationship
    item = db.relationship('Item', backref=db.backref('catalogues', lazy=True))

