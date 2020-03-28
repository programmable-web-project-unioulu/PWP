from flask import Blueprint, redirect
from flask_restful import Api
from src.resources.entrypoint import EntryPoint
from src.resources.articleresource import ArticleCollection, ArticleItem
from src.resources.userresource import UserCollection, UserItem
from src.resources.addedarticleresource import AddedArticleCollection, AddedArticleItem

APIARY_URL = "https://floridamangenerator.docs.apiary.io/#reference/"

api_bp = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_bp)

api.add_resource(EntryPoint, "/api/")
api.add_resource(ArticleCollection, "/api/articles/")
api.add_resource(ArticleItem, "/api/articles/<date>/")
api.add_resource(UserCollection, "/api/users/")
api.add_resource(UserItem, "/api/users/<username>/")
api.add_resource(AddedArticleCollection, "/api/addedarticles/")
api.add_resource(AddedArticleItem, "/api/addedarticles/<id>/", "/api/addedarticles/?owner=<user>")

@api_bp.route("/floridaman/link-relations/")
def redirect_to_apiary_link_rels():
    return redirect(APIARY_URL + "link-relations")

@api_bp.route("/profiles/articles/")
def redirect_to_articles_profile():
    return redirect(APIARY_URL + "profiles")

@api_bp.route("/profiles/users/")
def redirect_to_users_profile():
    return redirect(APIARY_URL + "profiles")

@api_bp.route("/profiles/addedarticles/")
def redirect_to_addedarticles_profile():
    return redirect(APIARY_URL + "profiles")
