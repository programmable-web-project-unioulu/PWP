"""
    Contains all the resources that are used to access the Facts model in the database.
"""


import json
from jsonschema import validate, ValidationError
from werkzeug.exceptions import BadRequest, UnsupportedMediaType, NotFound
from flask import Response, request, url_for
from flask_restful import Resource
from dogdict.models import Breed, Facts, db
from dogdict.constants import JSON
from dogdict.resources.mason import MasonBuilder

class FactBuilder(MasonBuilder):
    """
    Creates link relations for the Facts resource.
    These include POST, GET and DELETE methods.
    """

    def add_control_all_facts(self):
        self.add_control(
            "facts:facts-all",
            url_for(FactCollection),
            title="All facts",
            method="GET"
        )

    def add_control_add_facts(self):
        self.add_control_post(
            "facts:add-fact",
            "Add a new fact and connects it to an existing breed",
            url_for(FactCollection),
            FactItem.json_schema()
        )

    def add_control_delete_facts(self, fact_id):
        self.add_control(
            "fact:delete",
            url_for(FactItem, fact=fact_id),
            method="DELETE"
        )


class FactCollection(Resource):
    """
        Used to access all the Facts in the database at once.
    """

    def get(self):
        """
            GETs all the facts from the database
        """
        body = {"items": []}
        for db_fact in Facts.query.all():
            item = db_fact.serialize()
            body["items"].append(item)
        return Response(json.dumps(body), 200, mimetype=JSON)

    def post(self):
        """
            Used to validate a new fact against the correct Fact JSON schema
        """
        if not request.is_json:
            raise UnsupportedMediaType
        try:
            validate(request.json, Facts.json_schema())
        except ValidationError as exc:
            raise BadRequest(description=str(exc))

        breed = Breed.query.filter_by(name=request.json["breed"]).first()

        if not breed:
            # return ValueError("Breed '{breed}' does not exist".format(**request.json))
            return "Breed does not exist", 404

        fact = Facts(breed=breed, fact=request.json["fact"])

        db.session.add(fact)
        db.session.commit()
        """
        More information about url_for comment in course lovelace 
        https://lovelace.oulu.fi/ohjelmoitava-web/ohjelmoitava-web/flask-api-project-layout/#avoiding-circular-imports
        """
    
        uri_id = fact.id

        return Response(
            status=201, headers={"Item": url_for("api.factcollection", fact=fact),
                                "Location": url_for("api.factitem", fact=uri_id)}
        )


class FactItem(Resource):
    """
        Used to access a singular fact item
    """

    def delete(self, fact):
        """
            Deletes a single specific fact from the database.
        """
        try:
            db.session.delete(fact)
            db.session.commit()
            return Response(f"Successfully deleted fact {fact}", status=204)
        except:
            return "Fact not found!", 404
