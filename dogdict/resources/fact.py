import json
from jsonschema import validate, ValidationError
from werkzeug.exceptions import BadRequest, UnsupportedMediaType
from flask import Response, request, url_for
from flask_restful import Resource
from dogdict.models import Breed, Facts, db
from dogdict.constants import JSON

class FactCollection(Resource):

    def get(self):
        body = {"items": []}
        for db_fact in Facts.query.all():
            item = db_fact.serialize()
            body["items"].append(item)
        return Response(json.dumps(body), 200, mimetype=JSON)

    def post(self):
        if not request.is_json:
            raise UnsupportedMediaType
        try:
            validate(request.json, Facts.json_schema())
        except ValidationError as e:
            raise BadRequest(description=str(e))

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
        return Response(
            status=201, headers={"Item": url_for("api.factcollection", fact=fact)} # have to change this
        )

class FactItem(Resource):
    def delete(self, fact):
        try:
            db.session.delete(fact)
            db.session.commit()
            return Response(status=204)
        except:
            return "moro", 404