from flask import request, json, Response, Flask
from flask_restful import Api, Resource
from jsonschema import validate, ValidationError
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from src.builders.articlebuilder import ArticleBuilder
from src.builders.masonbuilder import MasonBuilder
from db.db import Articles

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

LINK_RELATIONS_URL = "/floridaman/link-relations/"
MASON = "application/vnd.mason+json"

class ArticleCollection(Resource):
    def get(self):
        body = ArticleBuilder(items = [])
        body.add_namespace("floman", LINK_RELATIONS_URL)
        for article in Articles.query.all():
            item = MasonBuilder(
                date=article.date,
                link=article.link,
                headline=article.headline
            )
            item.add_control("self", api.url_for(ArticleItem, date=article.date))
            item.add_control("profile", "/profiles/articles/")
            body["items"].append(item)
        body.add_control_add_article()
        ## Tähän pitää kirjotella article-by-id
        return Response(json.dumps(body), 200, mimetype=MASON)

    def post(self):
        if not request.json:
            return ArticleBuilder.create_error_response(415, "Unsupported media type", "Requests must be JSON")
        try:
            validate(request.json, ArticleBuilder.article_schema())
        except ValidationError as e:
            return ArticleBuilder.create_error_response(400, "Invalid JSON document", str(e))
        article = Articles(
            date = request.json["date"],
            link = request.json["link"],
            headline = request.json["headline"]
        )
        try:
            db.session.add(article)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return ArticleBuilder.create_error_response(409, "Already exists", "Product with date '{}' already exists.".format(request.json["date"]))
        return Response(status=201, headers={
            "Location": api.url_for(ArticleItem, date=request.json["date"])
        })

class ArticleItem(Resource):
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
