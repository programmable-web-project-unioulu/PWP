from flask import request, Response, json
from masonbuilder import MasonBuilder

class ArticleBuilder(MasonBuilder):
    @staticmethod
    def create_error_response(status_code, title, message=None):
        resource_url = request.path
        body = MasonBuilder(resource_url=resource_url)
        body.add_error(title, message)
        return Response(json.dumps(body), status_code, mimetype=MASON)

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

    def add_control_all_articles(self):
        self.add_control(
            "floman:articles-all",
            href='/api/articles/',
            method="GET"
        )

    def add_control_delete_article(self, date):
        self.add_control(
            "floman:delete",
            href='/api/articles/{}/'.format(date),
            method="DELETE"
        )

    def add_control_add_article(self):
        self.add_control(
            "floman:add-article",
            "/api/articles/",
            method="POST",
            encoding="json",
            schema=self.article_schema()
        )

    def add_control_edit_article(self, date):
        self.add_control(
            "edit",
            href='/api/articles/{}/'.format(date),
            method="PUT",
            encoding="json",
            schema=self.article_schema()
        )
