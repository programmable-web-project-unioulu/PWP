import json
from jsonschema import validate, ValidationError
from flask import Response, request, url_for
from werkzeug.exceptions import NotFound, Conflict, BadRequest, UnsupportedMediaType
from sqlalchemy.exc import IntegrityError
from flask_restful import Resource
from dogdict.models import Group, db
from dogdict.constants import JSON

class GroupCollection(Resource):

    def get(self):
        body = {"items": []}
        for db_group in Group.query.all():
            item = db_group.serialize()
            body["items"].append(item)

        return Response(json.dumps(body), 200, mimetype=JSON)

    def post(self):
        if not request.is_json:
            raise UnsupportedMediaType
        
        try:
            validate(request.json, Group.json_schema())
        except ValidationError as e:
            raise BadRequest(description=str(e))

        group = Group(name=request.json["name"])
        
        try:
            
            db.session.add(group)
            db.session.commit()
        except IntegrityError:
            raise Conflict(
                "Group with name '{name}' already exists.".format(
                    **request.json
                )
            )

        return Response(
            status=201, headers={"Item": url_for("api.groupcollection", group=group)}
        )


class GroupItem(Resource):
    def get(self, group):
        group = Group.query.filter_by(name=group.name).first()
        body = {
            "name": group.name
        }
        print(group.name)
        return Response(json.dumps(body), 200, mimetype=JSON)

    def put(self, group):
        print("GROUP222", group)
        if not request.is_json:
            return "", 415
        try:
            validate(request.json, Group.json_schema())

        except ValidationError as exc:
            raise BadRequest(description=str(exc)) from exc

        group = Group.query.filter_by(name=group.name).first()
        group.deserialize(request.json)

        db.session.add(group)
        db.session.commit()
        
        return Response(status=204)