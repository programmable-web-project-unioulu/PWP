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

    def add_control_all_facts(self, group, breed):
        uri_name = breed
        if " " in uri_name:
            uri_name = uri_name.replace(" ", "%20")
        self.add_control(
            "facts:facts-all",
            url_for("api.factcollection", group=group, breed=uri_name),
            title="All facts",
            method="GET"
        )

    def add_control_add_facts(self, group, breed):
        uri_name = breed
        if " " in uri_name:
            uri_name = uri_name.replace(" ", "%20")
        self.add_control_post(
            "facts:add-fact",
            "Add a new fact and connects it to an existing breed",
            url_for("api.factcollection", group=group, breed=uri_name),
            Facts.json_schema()
        )

    def add_control_delete_facts(self, fact_id, breed, group):
        uri_name = breed
        if " " in uri_name:
            uri_name = uri_name.replace(" ", "%20")
        print("this is add control delete fact:", fact_id, breed, group)
        self.add_control(
            "fact:delete",
            url_for("api.factitem", fact=fact_id, breed=uri_name, group=group),
            method="DELETE"
        )


class FactCollection(Resource):
    """
        Used to access all the Facts in the database at once.
    """

    def get(self, group, breed):
        """
            GETs all the facts from the database
        """
        body = FactBuilder(items=[])
        body.add_namespace("breeds", "/api/<group:group>/<breed:breed>/facts/")

        uri_name = breed.name
        if " " in uri_name:
            uri_name = uri_name.replace(" ", "%20")
        
        body.add_control("self", href=url_for("api.factcollection", breed=breed.name, group=group.name))
        body.add_control_all_facts(group.name, uri_name)
        body.add_control_add_facts(group.name, uri_name)

        for db_fact in Facts.query.filter_by(breed=breed):
            item = db_fact.serialize(short_form=True)
            body["items"].append(item)
            item["@controls"] = {
                "self": {"href": url_for("api.factitem", breed=uri_name, group=group.name, fact=db_fact.id)}
            }
        return Response(json.dumps(body), 200, mimetype=JSON)

    def post(self, group, breed):
        """
            Used to validate a new fact against the correct Fact JSON schema
        """
        print("THIS IS BREED:", breed.name)

        if not request.is_json:
            raise UnsupportedMediaType
        try:
            validate(request.json, Facts.json_schema_postput())
        except ValidationError as exc:
            raise BadRequest(description=str(exc))

        body = {"items": []}
        for db_fact in Facts.query.filter_by(breed=breed):
            item = db_fact.serialize(short_form=True)
            body["items"].append(item)
        
        # Check if the new fact value is already present in the list
        if any(item["fact"] == request.json["fact"]  for item in body["items"]):
            return "The fact is already connected to the breed!", 409

        db_breed = Breed.query.filter_by(name=breed.name).first()

        if not db_breed:
            # return ValueError("Breed '{breed}' does not exist".format(**request.json))
            return "Breed does not exist", 404

        fact = Facts(breed=db_breed, fact=request.json["fact"])

        db.session.add(fact)
        db.session.commit()
        """
        More information about url_for comment in course lovelace 
        https://lovelace.oulu.fi/ohjelmoitava-web/ohjelmoitava-web/flask-api-project-layout/#avoiding-circular-imports
        """

        uri_id = fact.id

        return Response(
            status=201, headers={"Item": url_for("api.factcollection", fact=fact, group=group.name, breed=breed.name),
                                 "Location": url_for("api.factitem", fact=uri_id,  group=group.name, breed=breed.name)}
        )


class FactItem(Resource):
    """
        Used to access a singular fact item
    """

    def get(self, group, breed, fact):
        body = FactBuilder(items=[])
    
        uri_name = breed.name
        if " " in uri_name:
            uri_name = uri_name.replace(" ", "%20")

        body.add_namespace("fact", f"/api/{group.name}/{uri_name}/facts/{fact.id}")

        body.add_control("self", href=url_for("api.factitem", breed=uri_name, group=group.name, fact=fact.id))
        print("HERE WE GOO ", fact.id, uri_name, group.name)
        body.add_control_delete_facts(fact.id, breed.name, group.name)

        print(fact)
        if fact == None:
            return Response("Fact not found", 404)
        body = {"items": [fact.fact]}
        return Response(json.dumps(body), 200, mimetype=JSON)

    def put(self, group, breed, fact):
        if not request.is_json:
            raise UnsupportedMediaType
        try:
            validate(request.json, Facts.json_schema_postput())
        except ValidationError as exc:
            raise BadRequest(description=str(exc)) from exc
        fact.deserialize(request.json)
        if fact.deserialize(request.json):
            fact = request.json["fact"]
            print("ASDASD", fact)

        db.session.add(fact)
        db.session.commit()
        return Response(json.dumps({"fact": fact.fact}), 204, mimetype=JSON)
    

    def delete(self, fact, group, breed):
        """
            Deletes a single specific fact from the database.
        """
        try:
            db.session.delete(fact)
            db.session.commit()
            return Response(f"Successfully deleted fact {fact}", status=204)
        except:
            return "Fact not found!", 404
