import click

from flask.cli import with_appcontext

from inventorymanager import db

# Association table for a many-to-many relationship between Items and Warehouses
# From https://lovelace.oulu.fi/ohjelmoitava-web/ohjelmoitava-web/introduction-to-web-development/#structure-of-databases
items_warehouses_association = db.Table('items_warehouses',
    db.Column('item_id', db.Integer, db.ForeignKey('item.id'), primary_key=True),
    db.Column('warehouse_id', db.Integer, db.ForeignKey('warehouse.id'), primary_key=True)
)

# Location model
class Location(db.Model):
    location_id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    country = db.Column(db.String(64), nullable=False, default="Finland")
    postal_code = db.Column(db.String(8), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    street = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return (f"<Location {self.id}, {self.city}, {self.country}, "
                f"Latitude: {self.latitude}, Longitude: {self.longitude}, "
                f"Postal Code: {self.postal_code}, Street: {self.street_name} {self.house_number}>")

# Warehouse model
class Warehouse(db.Model):
    warehouse_id = db.Column(db.Integer, primary_key=True)
    manager = db.Column(db.String(64), nullable=True)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id', ondelete='CASCADE'), nullable=True)
    location = db.relationship('Location', backref=db.backref('warehouses', lazy=True))

    # Many-to-many relationship with Items
    items = db.relationship('Item', secondary=items_warehouses_association, back_populates="warehouses")

    def __repr__(self):
        return f"<Warehouse(id={self.id}, manager='{self.manager}', location_id={self.location_id})>"

# Item model
class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    category = db.Column(db.String(64), nullable=True)
    weight = db.Column(db.Float, nullable=True)

    # Many-to-many relationship with Warehouses
    warehouses = db.relationship('Warehouse', secondary=items_warehouses_association, back_populates="items")

    def __repr__(self): 
        return f"<Item(id={self.id}, name='{self.name}', category='{self.category}', weight={self.weight})>"

# Stock model
class Stock(db.Model):
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouse.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    shelf_price = db.Column(db.Float, nullable=True)

    # Relationship
    item = db.relationship('Item', backref=db.backref('stocks', lazy=True))
    warehouse = db.relationship('Warehouse', backref=db.backref('stocks', lazy=True))

    def __repr__(self):
        return f"<Stock(item_id={self.item_id}, warehouse_id={self.warehouse_id}, quantity={self.quantity}, shelf_price={self.shelf_price})>"
    
# Catalogue model
class Catalogue(db.Model):
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    supplier_name = db.Column(db.String(64), primary_key=True)
    min_order = db.Column(db.Integer, nullable=False)
    order_price = db.Column(db.Float, nullable=True)

    # Relationship
    item = db.relationship('Item', backref=db.backref('catalogues', lazy=True))
    def __repr__(self):
        return f"<Catalogue(item_id={self.item_id}, supplier_name='{self.supplier_name}', min_order={self.min_order}, order_price={self.order_price})>"
    

@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    Initializes the database
    """
    db.create_all()

@click.command("populate-db")
@with_appcontext
def create_dummy_data():
    """
    Adds dummy data to the database
    """
    # Create dummy locations
    locations = [
        Location(latitude=60.1699, longitude=24.9384, country="Finland", postal_code="00100", city="Helsinki", street_name="Mannerheimintie", house_number=1),
        Location(latitude=60.4518, longitude=22.2666, country="Finland", postal_code="20100", city="Turku", street_name="Aurakatu", house_number=2),
    ]

    # Create dummy warehouses
    warehouses = [
        Warehouse(manager="John Doe", location=locations[0]),
        Warehouse(manager="Jane Doe", location=locations[1]),
    ]

    # Create dummy items
    items = [
        Item(name="Laptop", category="Electronics", weight=1.5),
        Item(name="Smartphone", category="Electronics", weight=0.2),
    ]

    # Create dummy stocks
    stocks = [
        Stock(item=items[0], warehouse=warehouses[0], quantity=10, shelf_price=999.99),
        Stock(item=items[1], warehouse=warehouses[1], quantity=20, shelf_price=599.99),
    ]

    # Create dummy catalogues
    catalogues = [
        Catalogue(item=items[0], supplier_name="TechSupplier A", min_order=5, order_price=950.00),
        Catalogue(item=items[1], supplier_name="TechSupplier B", min_order=10, order_price=550.00),
    ]

    # Add all to session and commit
    db.session.add_all(locations + warehouses + items + stocks + catalogues)
    db.session.commit()
    