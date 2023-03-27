"""
    Contains all the resources that are used to access the Breed model in the database.
"""
import json
import os
from jsonschema import validate, ValidationError
from flask import Response, request, url_for
from werkzeug.exceptions import Conflict, BadRequest, UnsupportedMediaType
from sqlalchemy.exc import IntegrityError
from flask_restful import Resource
from dogdict.models import Breed, Group, db
from dogdict.constants import JSON
from flasgger import Swagger, swag_from
from flasgger.utils import swag_from
from dogdict.resources.mason import MasonBuilder


class BreedBuilder(MasonBuilder):
    """
    Creates link relations for the Breed resource.
    These include POST, GET, DELETE and PUT methods.
    """

    def add_control_all_breeds(self):
        self.add_control(
            "breeds:breeds-all",
            url_for("api.breedcollection"),
            title="All breeds",
            method="GET"
        )

    def add_control_delete_breed(self, breed):
        self.add_control(
            "breed:delete",
            url_for("api.breeditem", breed=breed),
            method="DELETE"
        )

    def add_control_add_breeds(self):
        self.add_control_post(
            "breeds:add-breed",
            "Add a new breed and connects it to an existing group",
            url_for("api.breedcollection"),
            Breed.json_schema()
        )

    def add_control_edit_breed(self, breed):
        self.add_control_put(
            "breed:edit",
            url_for("api.breeditem", breed=breed),
            Breed.json_schema(),
        )


class BreedCollection(Resource):
    """
        Used to access multiple breeds at once.
    """
    # @swag_from("../doc/breedcollection/breeds_get.yml")

    def get(self):
        """
            Used to access ALL the breeds at once.
        """
        body = BreedBuilder(items=[])
        body.add_namespace("breeds", "/api/breeds/")
        body.add_control("self", href=url_for("api.breedcollection"))
        body.add_control_add_breeds()
        body.add_control_all_breeds()

        for db_breed in Breed.query.all():
            db_breed_serialised = db_breed.serialize()
            print("DB BREED SERIALISED", db_breed_serialised)
            item = {
                "name": db_breed_serialised["name"],
                "id": db_breed_serialised["id"],
            }
            item["@controls"] = {
                "self": {"href": url_for("api.breedcollection", breed=db_breed.name)}
            }
            body["items"].append(item)

        return Response(json.dumps(body), 200, mimetype=JSON)

    def post(self):
        """
            Used to POST a breed into the breed collection and to make sure it fits the schema.
        """
        if not request.is_json:
            raise UnsupportedMediaType
        try:
            validate(request.json, Breed.json_schema())
        except ValidationError as exc:
            raise BadRequest(description=str(exc))
        group = Group.query.filter_by(name=request.json["group"]).first()

        if not group:
            # return ValueError("Group '{group}' does not exist".format(**request.json))
            return "Group does not exist", 400

        breed = Breed(group=group, name=request.json["name"])

        try:
            db.session.add(breed)
            db.session.commit()
        except IntegrityError:
            return "Breed already exists", 409

        return Response(
            status=201, headers={"Location": url_for("api.breeditem", breed=breed.name)}
        )


class BreedItem(Resource):
    """
        Used to access specific breeds from the database.
    """

    def get(self, breed):
        """
            GETs a specific breed
        """
        body = BreedBuilder(items=[])
        body.add_namespace("breeds", f"/api/breeds/{breed.name}/")
        body.add_control("self", href=url_for(
            "api.breeditem", breed=breed.name))
        body.add_control_edit_breed(breed.name)
        body.add_control_delete_breed(breed.name)
        breed = Breed.query.filter_by(id=breed.id).first()

        group_info = {
            "name": breed.group.name,
            "id": breed.group.id
        }
        fact_info = []
        print("breed.facts", breed.facts)
        for i in breed.facts:
            fact_info.append(i.fact)


        item = breed.serialize()

        item["@controls"] = {
            "self": {"href": url_for("api.breeditem", breed=breed.name)}
        }
        body["items"].append(item)

        return Response(json.dumps(body), 200, mimetype=JSON)

    def put(self, breed):
        """
            Changes the values of an existing singular breed.
        """
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
        """
            DELETEs one single breed.
        """
        try:
            db.session.delete(breed)
            db.session.commit()
            return Response(status=204)
        except Exception:
            return "Breed not found!", 404
