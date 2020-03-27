from flask import request, Response, json
from masonbuilder import MasonBuilder

MASON = "application/vnd.mason+json"

class UserBuilder(MasonBuilder):
    @staticmethod
    def create_error_response(status_code, title, message=None):
        resource_url = request.path
        body = MasonBuilder(resource_url=resource_url)
        body.add_error(title, message)
        return Response(json.dumps(body), status_code, mimetype=MASON)

    @staticmethod
    def user_schema():
        schema = {
            "type": "object",
            "required": ["username"]
        }
        props = schema["properties"] = {}
        props["username"] = {
            "type": "string"
        }
        return schema

    def add_control_all_users(self):
        self.add_control(
            "floman:users-all",
            href='/api/articles/',
            method="GET"
        )

    def add_control_user_by_name(self, username):
        self.add_control(
            "floman:user-by-name",
            href='/api/users/{}/'.format(username),
            method='GET'
        )

    def add_control_owned_article(self, username):
        self.add_control(
            "floman:owned-articles",
            href='/api/addedarticles/?owner={}'.format(username),
            method='GET'
        )

    def add_control_delete_user(self, username):
        self.add_control(
            "floman:delete",
            href='/api/users/{}/'.format(username),
            method="DELETE"
        )

    def add_control_add_user(self):
        self.add_control(
            "floman:add-user",
            "/api/users/",
            method="POST",
            encoding="json",
            schema=self.user_schema()
        )

    def add_control_edit_user(self, username):
        self.add_control(
            "edit",
            href='/api/uers/{}/'.format(username),
            method="PUT",
            encoding="json",
            schema=self.user_schema()
        )
