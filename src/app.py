from flask import Flask
from flask_restful import Api
from src.resources.entrypoint import EntryPoint
from src.resources.articleresource import ArticleCollection, ArticleItem
from src.resources.userresource import UserCollection, UserItem

app = Flask(__name__)
api = Api(app)

api.add_resource(EntryPoint, "/api/")
api.add_resource(ArticleCollection, "/api/articles/")
api.add_resource(ArticleItem, "/api/articles/<date>/")
api.add_resource(UserCollection, "/api/users/")
api.add_resource(UserItem, "/api/users/<username>/")

@app.route("/floridaman/link-relations/")
def send_link_relations_html():
    return "Terve"

@app.route("/profiles/product/")
def send_profiles_html():
    return "Moro"