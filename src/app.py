from flask import Flask, request, json, abort, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_restful import Api, Resource
from jsonschema import validate, ValidationError

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

LINK_RELATIONS_URL = "/storage/link-relations/"
MASON = "application/vnd.mason+json"

class MasonBuilder(dict):
    """
    A convenience class for managing dictionaries that represent Mason
    objects. It provides nice shorthands for inserting some of the more
    elements into the object but mostly is just a parent for the much more
    useful subclass defined next. This class is generic in the sense that it
    does not contain any application specific implementation details.
    """

    def add_error(self, title, details):
        """
        Adds an error element to the object. Should only be used for the root
        object, and only in error scenarios.

        Note: Mason allows more than one string in the @messages property (it's
        in fact an array). However we are being lazy and supporting just one
        message.

        : param str title: Short title for the error
        : param str details: Longer human-readable description
        """

        self["@error"] = {
            "@message": title,
            "@messages": [details],
        }

    def add_namespace(self, ns, uri):
        """
        Adds a namespace element to the object. A namespace defines where our
        link relations are coming from. The URI can be an address where
        developers can find information about our link relations.

        : param str ns: the namespace prefix
        : param str uri: the identifier URI of the namespace
        """

        if "@namespaces" not in self:
            self["@namespaces"] = {}

        self["@namespaces"][ns] = {
            "name": uri
        }

    def add_control(self, ctrl_name, href, **kwargs):
        """
        Adds a control property to an object. Also adds the @controls property
        if it doesn't exist on the object yet. Technically only certain
        properties are allowed for kwargs but again we're being lazy and don't
        perform any checking.

        The allowed properties can be found from here
        https://github.com/JornWildt/Mason/blob/master/Documentation/Mason-draft-2.md

        : param str ctrl_name: name of the control (including namespace if any)
        : param str href: target URI for the control
        """

        if "@controls" not in self:
            self["@controls"] = {}

        self["@controls"][ctrl_name] = kwargs
        self["@controls"][ctrl_name]["href"] = href


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

class InventoryBuilder(MasonBuilder):
    @staticmethod
    def create_error_response(status_code, title, message=None):
        resource_url = request.path
        body = MasonBuilder(resource_url=resource_url)
        body.add_error(title, message)
        return Response(json.dumps(body), status_code, mimetype=MASON)

    @staticmethod
    def product_schema():
        schema = {
            "type": "object",
            "required": ["handle", "weight", "price"]
        }
        props = schema["properties"] = {}
        props["handle"] = {
            "type": "string"
        }
        props["weight"] = {
            "type": "number"
        }
        props["price"] = {
            "type": "number"
        }
        return schema

    def add_control_all_products(self):
        self.add_control(
            "storage:products-all",
            href='/api/products/',
            method="GET"
        )

    def add_control_delete_product(self, handle):
        self.add_control(
            "storage:delete",
            href='/api/products/{}/'.format(handle),
            method="DELETE"
        )

    def add_control_add_product(self):
        self.add_control(
            "storage:add-product",
            "/api/products/",
            method="POST",
            encoding="json",
            schema=self.product_schema()
        )

    def add_control_edit_product(self, handle):
        self.add_control(
            "edit",
            href='/api/products/{}/'.format(handle),
            method="PUT",
            encoding="json",
            schema=self.product_schema()
        )

class EntryPoint(Resource):
    def get(self):
        body = MasonBuilder()
        body.add_namespace("storage", LINK_RELATIONS_URL)
        body.add_control("storage:products-all", api.url_for(ProductCollection))
        return Response(json.dumps(body), 200, mimetype=MASON)

class ProductCollection(Resource):
    def get(self):
        body = InventoryBuilder(items = [])
        body.add_namespace("storage", LINK_RELATIONS_URL)
        for products in Product.query.all():
            item = MasonBuilder(
                handle=products.handle,
                weight=products.weight,
                price=products.price
            )
            item.add_control("self", api.url_for(ProductItem, handle=products.handle))
            item.add_control("profile", "/profiles/product/")
            body["items"].append(item)
        body.add_control("self", "/api/products/")
        body.add_control_add_product()
        return Response(json.dumps(body), 200, mimetype=MASON)

    def post(self):
        if not request.json:
            return InventoryBuilder.create_error_response(415, "Unsupported media type", "Requests must be JSON")
        try:
            validate(request.json, InventoryBuilder.product_schema())
        except ValidationError as e:
            return InventoryBuilder.create_error_response(400, "Invalid JSON document", str(e))
        product = Product(
            handle = request.json["handle"],
            weight = request.json["weight"],
            price = request.json["price"]
        )
        try:
            db.session.add(product)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return InventoryBuilder.create_error_response(409, "Already exists", "Product with handle '{}' already exists.".format(request.json["handle"]))
        return Response(status=201, headers={
            "Location": api.url_for(ProductItem, handle=request.json["handle"])
        })

class ProductItem(Resource):
    def get(self, handle):
        product = Product.query.filter_by(handle=handle).first()
        if product is None:
            return InventoryBuilder.create_error_response(404, "Not found", "Product with handle '{}' doesn't exist.".format(handle))
        body = InventoryBuilder(
            handle=product.handle,
            weight=product.weight,
            price=product.price
        )
        body.add_control("self", "/api/products/{}/".format(product.handle))
        body.add_control("profile", "/profiles/product/")
        body.add_control("collection", "/api/products/")
        body.add_control_edit_product(product.handle)
        body.add_control_delete_product(product.handle)
        return Response(json.dumps(body), 200, mimetype=MASON)

    def put(self, handle):
        if not request.json:
            return InventoryBuilder.create_error_response(415, "Unsupported media type", "Requests must be JSON")
        try:
            validate(request.json, InventoryBuilder.product_schema())
        except ValidationError as e:
            return InventoryBuilder.create_error_response(400, "Invalid JSON document", str(e))
        product = Product.query.filter_by(handle=handle).first()
        if product is None:
            return InventoryBuilder.create_error_response(404, "Not found", "Product with handle '{}' doesn't exist.".format(handle))
        product.handle = request.json["handle"]
        product.weight = request.json["weight"]
        product.price = request.json["weight"]
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return InventoryBuilder.create_error_response(409, "Already exists", "Product with handle '{}' already exists.".format(request.json["handle"]))
        return Response(status=204)

    def delete(self, handle):
        product = Product.query.filter_by(handle=handle).first()
        if product is None:
            return InventoryBuilder.create_error_response(404, "Not found", "Product with handle '{}' doesn't exist.".format(handle))
        db.session.delete(product)
        db.session.commit()
        return Response(status=204)

api.add_resource(EntryPoint, "/api/")
api.add_resource(ProductCollection, "/api/products/")
api.add_resource(ProductItem, "/api/products/<handle>/")

@app.route("/storage/link-relations/")
def send_link_relations_html():
    return "Terve"

@app.route("/profiles/product/")
def send_profiles_html():
    return "Moro"