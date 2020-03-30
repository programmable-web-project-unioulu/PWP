from flask import request, json, Response, Flask
from flask_restful import Api, Resource
from jsonschema import validate, ValidationError
from sqlalchemy.exc import IntegrityError
from src.builders.articlebuilder import ArticleBuilder
from src.builders.masonbuilder import MasonBuilder
from db.db import Articles

LINK_RELATIONS_URL = "/floridaman/link-relations/"
MASON = "application/vnd.mason+json"

app = Flask(__name__)
api = Api(app)

class ArticleCollection(Resource):
    def get(self):
        body = ArticleBuilder(items = [])
        body.add_namespace("floman", LINK_RELATIONS_URL)
        body.add_control("profile", "/profiles/articles/")
        body.add_control_add_article()
        body.add_control_article_by_date()
        for article in Articles.query.all():
            item = MasonBuilder(
                date=article.date,
                link=article.link,
                headline=article.headline
            )
            body["items"].append(item)
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
            return ArticleBuilder.create_error_response(409, "Already exists", "Article with date '{}' already exists.".format(request.json["date"]))
        return Response(status=201, headers={
            "Location": api.url_for(ArticleItem, date=request.json["date"])
        })

class ArticleItem(Resource):
    def get(self, date):
        article = Articles.query.filter_by(date=date).first()
        if article is None:
            return ArticleBuilder.create_error_response(404, "Not found", "Article with date '{}' doesn't exist.".format(date))
        body = ArticleBuilder(
            date=article.date,
            link=article.link,
            headline=article.headline
        )
        body.add_control_all_articles()
        body.add_control("profile", "/profiles/articles/")
        body.add_control("self", "/api/articles/{}/".format(article.date))
        body.add_control_edit_article(article.date)
        body.add_control_delete_article(article.date)
        return Response(json.dumps(body), 200, mimetype=MASON)

    def put(self, date):
        if not request.json:
            return ArticleBuilder.create_error_response(415, "Unsupported media type", "Requests must be JSON")
        try:
            validate(request.json, ArticleBuilder.article_schema())
        except ValidationError as e:
            return ArticleBuilder.create_error_response(400, "Invalid JSON document", str(e))
        article = Articles.query.filter_by(date=date).first()
        if article is None:
            return ArticleBuilder.create_error_response(404, "Not found", "Article with date '{}' doesn't exist.".format(date))
        article.date = request.json["date"]
        article.link = request.json["link"]
        article.headline = request.json["headline"]
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return ArticleBuilder.create_error_response(409, "Already exists", "Article with date '{}' already exists.".format(request.json["date"]))
        return Response(status=204)

    def delete(self, date):
        article = Articles.query.filter_by(date=date).first()
        if article is None:
            return ArticleBuilder.create_error_response(404, "Not found", "Article with date '{}' doesn't exist.".format(date))
        db.session.delete(article)
        db.session.commit()
        return Response(status=204)
