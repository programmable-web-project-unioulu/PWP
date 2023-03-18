import json
from jsonschema import validate, ValidationError
from flask import Response, request, url_for
from werkzeug.exceptions import Conflict, BadRequest, UnsupportedMediaType
from sqlalchemy.exc import IntegrityError
from flask_restful import Resource
from dogdict.models import Breed, Group, db
from dogdict.constants import JSON

class BreedCollection(Resource):

    def get(self):
        body = {"items": []}
        for db_breed in Breed.query.all():
            item = db_breed.serialize()
            body["items"].append(item)
        return Response(json.dumps(body), 200, mimetype=JSON)

    def post(self):
        if not request.is_json:
            raise UnsupportedMediaType
        try:
            print(request.json,"moroo")
            validate(request.json, Breed.json_schema())
        except ValidationError as e:
            raise BadRequest(description=str(e))
        
        group = Group.query.filter_by(name=request.json["group"]).first()

        if not group:
            # return ValueError("Group '{group}' does not exist".format(**request.json))
            return "Group does not exist", 400

        breed = Breed(group=group, name=request.json["name"])

        try:
            db.session.add(breed)
            db.session.commit()
        except IntegrityError:
            raise Conflict(
                "Breed with name '{name}' already exists.".format(
                    **request.json
                )
            )

        return Response(
            status=201, headers={"Item": url_for("api.breedcollection", breed=breed)}
        )

class BreedItem(Resource):

    def get(self, breed):
        if "404" in str(breed):
            return "", 404
        else:
            return Response(json.dumps(breed.serialize()), 200, mimetype=JSON)

    def put(self, breed):
        if not request.is_json:
            raise UnsupportedMediaType

        try:
            validate(request.json, Breed.json_schema())
        except ValidationError as exc:
            raise BadRequest(description=str(exc)) from exc
        breed.deserialize(request.json)
        db.session.add(breed)
        db.session.commit()
        print(breed.serialize())
        return Response(json.dumps(breed.serialize()), 204, mimetype=JSON)

    def delete(self, breed):
        try:
            db.session.delete(breed)
            db.session.commit()
            return Response(status=204)
        except:
            return "moro", 404