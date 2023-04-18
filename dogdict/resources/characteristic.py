"""
    Contains all the resources that are used to access the Characteristics model in the database.
"""

import json
from jsonschema import validate, ValidationError
from werkzeug.exceptions import BadRequest, UnsupportedMediaType
from flask import Response, request, url_for
from flask_restful import Resource
from dogdict.models import Characteristics, Breed, db
from dogdict.constants import JSON
from dogdict.utils import check_for_space
from dogdict.resources.mason import MasonBuilder


class CharacteristicsBuilder(MasonBuilder):
    """
    Creates link relations for the Characteristics resource.
    These include POST and GET methods.
    """

    def add_control_all_characteristics(self, group, breed):
        uri_name = check_for_space(breed)
        self.add_control(
            "characteristics:characteristics-all",
            url_for("api.characteristiccollection", group=group, breed=uri_name),
            title="All characteristics",
            method="GET",
        )

    def add_control_add_characteristics(self, group, breed):
        uri_name = check_for_space(breed)
        self.add_control_post(
            "characteristics:add-characteristic",
            "Add a new characteristics and connects it to an existing breed",
            url_for("api.characteristiccollection", group=group, breed=uri_name),
            Characteristics.json_schema(),
        )

    def add_control_edit_characteristics(self, group, breed):
        uri_name = check_for_space(breed)
        self.add_control_put(
            "characteristics:edit",
            url_for("api.characteristiccollection", group=group, breed=uri_name),
            Characteristics.json_schema()
        )


class CharacteristicCollection(Resource):
    """
    Used to access all the characteristics at once.
    """

    def get(self, group, breed):
        """
        GETs all the characteristics
        """
        body = CharacteristicsBuilder(items=[])
        body.add_namespace(
            "breeds", "/api/groups/<group:group>/breeds/<breed:breed>/characteristics/")
        
        uri_name = check_for_space(breed.name)

        body.add_control(
            "self",
            href=url_for(
                "api.characteristiccollection", breed=breed.name, group=group.name
            ),
        )

        body.add_control_all_characteristics(group.name, uri_name)
        body.add_control_add_characteristics(group.name, uri_name)
        body.add_control_edit_characteristics(group.name, uri_name)

        print("this is group and breed", group, breed)
        for db_characteristics in Characteristics.query.join(
            Characteristics.in_breed
        ).filter_by(name=breed.name):
            item = db_characteristics.serialize(short_form=True)
            print("This is item", item)
            body["items"].append(item)
            item["@controls"] = {
                "self": {
                    "href": url_for(
                        "api.characteristiccollection", breed=uri_name, group=group.name
                    )
                }
            }
        return Response(json.dumps(body), 200, mimetype=JSON)

    def post(self, group, breed):
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

        print("breed.characteristics", breed.characteristics)
        if breed.characteristics is not None:
            return "Breed already has a characteristic", 409

        characteristics = Characteristics(
            in_breed=[breed], life_span=request.json["life_span"]
        )

        # to check if post request contains coat_length and exercise
        try:
            coat_length = request.json["coat_length"]
        except KeyError:
            coat_length = None
        try:
            exercise = request.json["exercise"]
        except KeyError:
            exercise = None
        # print(characteristics.in_breed, characteristics.life_span)
        if coat_length:
            print("Got here CL", coat_length)
            characteristics = Characteristics(
                in_breed=[breed],
                life_span=request.json["life_span"],
                coat_length=request.json["coat_length"],
            )
            if exercise:
                print("Got here CL, exercise", coat_length, exercise)
                characteristics = Characteristics(
                    in_breed=[breed],
                    life_span=request.json["life_span"],
                    coat_length=request.json["coat_length"],
                    exercise=request.json["exercise"],
                )

        elif exercise:
            print("Got here exercise", coat_length)
            characteristics = Characteristics(
                in_breed=[breed],
                life_span=request.json["life_span"],
                exercise=request.json["exercise"],
            )

        db.session.add(characteristics)
        db.session.commit()

        uri_id = characteristics.id

        print("This is char", breed.name, group.name)
        return Response(
            status=201,
            headers={
                "Item": url_for(
                    "api.characteristiccollection",
                    characteristics=characteristics,
                    breed=breed.name,
                    group=group.name,
                ),
                "Location": url_for(
                    "api.characteristiccollection",
                    characteristics=uri_id,
                    breed=breed.name,
                    group=group.name,
                ),
            },
        )

    def put(self, group, breed):
        """
        Change characteristics of one breed from given url
        put "/api/terrier/australian_terrier/charateristics/
        """
        if not request.is_json:
            raise UnsupportedMediaType
        print("this is request.json", request.json)
        try:
            validate(request.json, Characteristics.json_schema_for_put())
        except ValidationError as exc:
            print("THIS IS EXC", exc)
            raise BadRequest(description=str(exc)) from exc

        for characteristics in Characteristics.query.join(
            Characteristics.in_breed
        ).filter_by(name=breed.name):
            characteristics.deserialize(request.json)
        print(characteristics.serialize)
        db.session.add(characteristics)
        db.session.commit()
        return Response(
            json.dumps({"characteristics": request.json}), 204, mimetype=JSON
        )
