from flask import Flask, json, Response
from flask_restful import Api, Resource
from src.builders.masonbuilder import MasonBuilder
from src.resources.articleresource import ArticleCollection
from src.resources.userresource import UserCollection
from src.resources.addedarticleresource import AddedArticleCollection

LINK_RELATIONS_URL = "/floridaman/link-relations/"
MASON = "application/vnd.mason+json"

app = Flask(__name__)
api = Api(app)

class EntryPoint(Resource):
    def get(self):
        body = MasonBuilder()
        body.add_namespace("floman", LINK_RELATIONS_URL)
        body.add_control("floman:articles-all", api.url_for(ArticleCollection))
        body.add_control("floman:users-all", api.url_for(UserCollection))
        body.add_control("floman:addedarticles-all", api.url_for(AddedArticleCollection))
        return Response(json.dumps(body), 200, mimetype=MASON)
