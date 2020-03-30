## Builder for Articles

## import required libraries and classes from modules
from flask import request, Response, json
from src.builders.masonbuilder import MasonBuilder

## Set constants
MASON = "application/vnd.mason+json"

class ArticleBuilder(MasonBuilder):

    ## Static method to generate error message
    @staticmethod
    def create_error_response(status_code, title, message=None):
        resource_url = request.path
        body = MasonBuilder(resource_url=resource_url)
        body.add_error(title, message)
        return Response(json.dumps(body), status_code, mimetype=MASON)

    ## Static method to fetch the article schema
    @staticmethod
    def article_schema():
        schema = {
            "type": "object",
            "required": ["date", "headline"]
        }
        props = schema["properties"] = {}
        props["date"] = {
            "type": "string"
        }
        props["link"] = {
            "type": "string"
        }
        props["headline"] = {
            "type": "string"
        }
        return schema

    ## Static method to fetch the article by date schema
    @staticmethod
    def article_by_date_schema():
        schema = {
            "type": "object",
            "required": ["date"]
        }
        props = schema["properties"] = {}
        props["date"] = {
            "type": "string"
        }
        return schema

    ## Get all articles
    def add_control_all_articles(self):
        self.add_control(
            "floman:articles-all",
            href='/api/articles/',
            method="GET"
        )

    ## Get an article by date
    def add_control_article_by_date(self):
        self.add_control(
            "floman:article-by-date",
            href='/api/articles/<date>/',
            method='GET',
            encoding="json",
            schema=self.article_by_date_schema()
        )

    ## Delete an article
    def add_control_delete_article(self, date):
        self.add_control(
            "floman:delete",
            href='/api/articles/{}/'.format(date),
            method="DELETE"
        )

    ## Add new article
    def add_control_add_article(self):
        self.add_control(
            "floman:add-article",
            "/api/articles/",
            method="POST",
            encoding="json",
            schema=self.article_schema()
        )

    ## Edit existing article
    def add_control_edit_article(self, date):
        self.add_control(
            "edit",
            href='/api/articles/{}/'.format(date),
            method="PUT",
            encoding="json",
            schema=self.article_schema()
        )
