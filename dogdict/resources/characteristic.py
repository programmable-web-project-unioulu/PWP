"""
    Contains all the resources that are used to access the Characteristics model in the database.
"""

import json
from jsonschema import validate, ValidationError
from werkzeug.exceptions import Conflict, BadRequest, UnsupportedMediaType
from flask import Response, request, url_for
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from dogdict.models import Characteristics, Breed, db
from dogdict.constants import JSON


class CharacteristicCollection(Resource):
    """
        Used to access all the characteristics at once.
    """
    def get(self):
        """
            GETs all the characteristics
        """
        body = {"items": []}
        for db_characteristics in Characteristics.query.all():
            item = db_characteristics.serialize()
            body["items"].append(item)
        print(body["items"])
        return Response(json.dumps(body), 200, mimetype=JSON)

    def post(self):
        """
            Used to POST a characteristics into the collection
            and validate it against the Characteristics JSON schema.
        """
        if not request.is_json:
            raise UnsupportedMediaType

        try:
            validate(request.json, Characteristics.json_schema())
        except ValidationError as exc:
            raise BadRequest(description=str(exc))

        if request.json["life_span"] < 5:
            return "Life span is too short!", 400

        breed = Breed.query.filter_by(name=request.json["in_breed"]).first()

        if not breed:
            print("this is 404 breed does not exist")
            return "Breed does not exist", 404

        if breed.characteristics is not None:
            return "Breed already has a characteristic", 409
        
        characteristics = Characteristics(
            in_breed=[breed], life_span=request.json["life_span"])

        # to check if post request contains coat_length and exercise
        try:
            coat_length = request.json["coat_length"]
        except KeyError:
            coat_length = None
        try:
            exercise = request.json["exercise"]
        except KeyError:
            exercise = None
        print(characteristics.in_breed, characteristics.life_span)
        if coat_length:
            characteristics = Characteristics(in_breed=[breed], life_span=request.json["life_span"],
                                              coat_length=request.json["coat_length"])

            if exercise:
                characteristics = Characteristics(in_breed=[breed],
                                                life_span=request.json["life_span"],
                                                coat_length=request.json["coat_length"],
                                                exercise=request.json["exercise"])

        if exercise:
            characteristics = Characteristics(in_breed=[breed],
                                              life_span=request.json["life_span"],
                                              exercise=request.json["exercise"])

        try:
            db.session.add(characteristics)
            db.session.commit()
        except IntegrityError as exc:
            raise Conflict(
                f"Characteristics for breed '{request.json}' already exists."
            )

        return Response(
            status=201, headers={"Item": url_for("api.characteristiccollection",
                                                characteristics=characteristics)}
        )
