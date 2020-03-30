from flask import request, json, Response, Flask
from flask_restful import Api, Resource
from jsonschema import validate, ValidationError
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from src.builders.userbuilder import UserBuilder
from src.builders.masonbuilder import MasonBuilder
from db.db import Users

app = Flask(__name__)
api = Api(app)

LINK_RELATIONS_URL = "/floridaman/link-relations/"
MASON = "application/vnd.mason+json"

class UserCollection(Resource):
    def get(self):
        body = UserBuilder(items = [])
        body.add_namespace("floman", LINK_RELATIONS_URL)
        body.add_control("profile", "/profiles/articles/")
        ## Tähän tulee user-by-name
        body.add_control_add_user()
        for user in Users.query.all():
            item = MasonBuilder(
                username=user.username
            )
            body["items"].append(item)
        return Response(json.dumps(body), 200, mimetype=MASON)

    def post(self):
        if not request.json:
            return UserBuilder.create_error_response(415, "Unsupported media type", "Requests must be JSON")
        try:
            validate(request.json, UserBuilder.user_schema())
        except ValidationError as e:
            return UserBuilder.create_error_response(400, "Invalid JSON document", str(e))
        user = Users(
            username = request.json["username"]
        )
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return UserBuilder.create_error_response(409, "Already exists", "User with username '{}' already exists.".format(request.json["username"]))
        return Response(status=201, headers={
            "Location": api.url_for(UserItem, username=request.json["username"])
        })

class UserItem(Resource):
    def get(self, username):
        user = Users.query.filter_by(username=username).first()
        if user is None:
            return UserBuilder.create_error_response(404, "Not found", "User with username '{}' doesn't exist.".format(username))
        body = UserBuilder(
            username=user.username
        )
        body.add_control_all_users()
        body.add_control("profile", "/profiles/users/")
        body.add_control("self", "/api/users/{}/".format(user.username))
        body.add_control_edit_user(user.username)
        body.add_control_delete_user(user.username)
        body.add_control_owned_article(user.username)
        return Response(json.dumps(body), 200, mimetype=MASON)

    def put(self, username):
        if not request.json:
            return UserBuilder.create_error_response(415, "Unsupported media type", "Requests must be JSON")
        try:
            validate(request.json, UserBuilder.user_schema())
        except ValidationError as e:
            return UserBuilder.create_error_response(400, "Invalid JSON document", str(e))
        user = Users.query.filter_by(username=username).first()
        if user is None:
            return UserBuilder.create_error_response(404, "Not found", "User with username '{}' doesn't exist.".format(username))
        user.username = request.json["username"]
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return UserBuilder.create_error_response(409, "Already exists", "User with username '{}' already exists.".format(request.json["username"]))
        return Response(status=204)

    def delete(self, username):
        user = Users.query.filter_by(username=username).first()
        if user is None:
            return UserBuilder.create_error_response(404, "Not found", "User with username '{}' doesn't exist.".format(username))
        db.session.delete(user)
        db.session.commit()
        return Response(status=204)
