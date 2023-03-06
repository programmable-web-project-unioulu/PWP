from flask import Flask, Response, request
import json
import os
from sqlalchemy.engine import Engine
from sqlalchemy import event
from sqlalchemy.exc import IntegrityError, OperationalError
from flask_restful import Api, Resource
from database import db, Group, Breed, Characteristics, Facts, app
from werkzeug.exceptions import NotFound, Conflict, BadRequest, UnsupportedMediaType
from werkzeug.routing import BaseConverter
from jsonschema import validate, ValidationError, draft7_format_checker

JSON = "application/json"

# app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)
api = Api(app)


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


class GroupCollection(Resource):

    def get(self):
        body = {"items": []}
        for db_group in Group.query.all():
            item = db_group.serialize()
            body["items"].append(item)

        return Response(json.dumps(body), 200, mimetype=JSON)

    def post(self):
        if not request.json:
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
            status=201, headers={"Item": api.url_for(GroupCollection, group=group)}
        )


class BreedCollection(Resource):

    def get(self):
        body = {"items": []}
        for db_breed in Breed.query.all():
            item = db_breed.serialize()
            body["items"].append(item)
        return Response(json.dumps(body), 200, mimetype=JSON)

    def post(self):
        if not request.json:
            raise UnsupportedMediaType

        try:
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
            status=201, headers={"Item": api.url_for(BreedCollection, breed=breed)}
        )


class FactCollection(Resource):

    def get(self):
        body = {"items": []}
        for db_fact in Facts.query.all():
            item = db_fact.serialize()
            body["items"].append(item)
        return Response(json.dumps(body), 200, mimetype=JSON)

    def post(self):
        if not request.json:
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

        return Response(
            status=201, headers={"Item": api.url_for(FactCollection, fact=fact)}
        )



class CharacteristicsCollection(Resource):

    def get(self):
        body = {"items": []}
        for db_characteristics in Characteristics.query.all():
            item = db_characteristics.serialize()
            body["items"].append(item)
        print(body["items"])
        return Response(json.dumps(body), 200, mimetype=JSON)

    def post(self):
        if not request.json:
            raise UnsupportedMediaType

        try:
            validate(request.json, Characteristics.json_schema())
        except ValidationError as e:
            raise BadRequest(description=str(e))

        breed = [Breed.query.filter_by(name=request.json["in_breed"]).first()]

        if not breed:
            # return ValueError("Breed '{breed}' does not exist".format(**request.json))
            return "Breed does not exist", 404

        characteristics = Characteristics(
            in_breed=breed, life_span=request.json["life_span"])

        # to check if post request contains coat_length and exercise
        try:
            coat_length = request.json["coat_length"]
        except KeyError:
            coat_length = None
        try:
            exercise = request.json["exercise"]
        except KeyError:
            exercise = None

        if coat_length:
            characteristics = Characteristics(in_breed=breed, life_span=request.json["life_span"],
                                              coat_length=request.json["coat_length"])

            if exercise:
                characteristics = Characteristics(in_breed=breed, life_span=request.json["life_span"],
                                                  coat_length=request.json["coat_length"],
                                                  exercise=request.json["exercise"])

        if exercise:
            characteristics = Characteristics(in_breed=breed, life_span=request.json["life_span"],
                                              exercise=request.json["exercise"])

        try:
            db.session.add(characteristics)
            db.session.commit()
        except IntegrityError:
            raise Conflict(
                "Characteristics for breed '{in_breed}' already exists.".format(
                    **request.json
                )
            )

        return Response(
            status=201, headers={"Item": api.url_for(CharacteristicsCollection, characteristics=characteristics)}
        )


class GroupItem(Resource):
    def get(self, group):
        group = Group.query.filter_by(name=group.name).first()
        body = {
            "name": group.name
        }
        print(group.name)
        return Response(json.dumps(body), 200, mimetype=JSON)

    def post(self, group):
        if not request.json:
            return "", 415

        try:
            validate(request.json, Facts.json_schema(),
                     format_checker=draft7_format_checker,
                     )
        except ValidationError as exc:
            raise BadRequest(description=str(exc)) from exc
    
    def put(self, group):
        print(group)
        if not request.json:
            return "", 415
        try:
            validate(request.json, Group.json_schema())
        
        except ValidationError as exc:
            raise BadRequest(description=str(exc)) from exc
        
        group = Group.query.filter_by(name=group.name).first()
        group.deserialize(request.json)

        try:
            db.session.add(group)
            db.session.commit()
        except IntegrityError as exc:
            group = Breed.query.filter_by(name=group.name).first()


class BreedItem(Resource):
    def get(self, group, breed):
        print(group, breed)
        pass

    def put(self, group, breed):
        # to be implemented
        if not request.json:
            raise UnsupportedMediaType

        try:
            validate(request.json, Breed.json_schema())
        except ValidationError as exc:
            raise BadRequest(description=str(exc)) from exc

        breed.deserialize(request.json)
        try:
            db.session.add(breed)
            db.session.commit()
        except IntegrityError as exc:
            group = Breed.query.filter_by(name=breed.name).first()

    def delete(self, breed):
        try:
            db.session.delete(breed)
            db.session.commit()
            return Response(status=204)
        except:
            return "moro", 404
        
class FactItem(Resource):

    def delete(self, fact):
        try:
            db.session.delete(fact)
            db.session.commit()
            return Response(status=204)
        except:
            return "moro", 404

class GroupConverter(BaseConverter):

    def to_python(self, value):
        print(value)
        value = value.capitalize() # add capitalization so URI does not need to be uppercase
        db_group = Group.query.filter_by(name=value).first()
        if db_group is None:
            raise NotFound
        return db_group

    def to_url(self, value):
        print("BREED:", value)
        return str(value)


class BreedConverter(BaseConverter):

    def to_python(self, value): # MARTTI MUUTTI TÄMÄN ID:LLÄ TOIMIVAKSI, MIETITÄÄN MITÄ TAPAHTUU
        db_breed = Breed.query.filter_by(id=value).first()
        if db_breed is None:
            raise NotFound
        return db_breed

    def to_url(self, value):
        print("BREED:", value)
        return str(value)

class FactConverter(BaseConverter):
    def to_python(self, value):
        db_fact = Facts.query.filter_by(id=value).first()
        if db_fact is None:
            raise NotFound
        return db_fact

    def to_url(self, value):
        print("fact:", value)
        return str(value)


app.url_map.converters["group"] = GroupConverter
app.url_map.converters["breed"] = BreedConverter
app.url_map.converters["fact"] = FactConverter

api.add_resource(GroupCollection, "/api/groups/")
api.add_resource(BreedCollection, "/api/breeds/")
api.add_resource(FactCollection, "/api/facts/")
api.add_resource(CharacteristicsCollection, "/api/characteristics/")

api.add_resource(GroupItem, "/api/groups/<group:group>/")
api.add_resource(BreedItem, "/api/breeds/<breed:breed>/")
api.add_resource(FactItem, "/api/facts/<fact:fact>/")

debug = True
"""
if os.environ['DOCKER'] == True:
    debug = False
"""
if __name__ == '__main__':
    app.run(debug=debug, host="0.0.0.0")
