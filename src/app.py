from flask import Flask, request, json, abort, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_restful import Api, Resource
from jsonschema import validate, ValidationError
from db.db import Articles, AddedArticles, Users
from builders.masonbuilder import MasonBuilder
from builders.addedarticlebuilder import AddedArticleBuilder
from builders.articlebuilder import ArticleBuilder
from builders.userbuilder import UserBuilder

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

LINK_RELATIONS_URL = "/floridaman/link-relations/"
MASON = "application/vnd.mason+json"

api.add_resource(EntryPoint, "/api/")
api.add_resource(ProductCollection, "/api/products/")
api.add_resource(ProductItem, "/api/products/<handle>/")

@app.route("/storage/link-relations/")
def send_link_relations_html():
    return "Terve"

@app.route("/profiles/product/")
def send_profiles_html():
    return "Moro"