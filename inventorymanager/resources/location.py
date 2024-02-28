"""
Code edited from course example
https://github.com/enkwolf/pwp-course-sensorhub-api-example/blob/master/sensorhub/resources/location.py
Examples from PWP course exercise 2
https://lovelace.oulu.fi/ohjelmoitava-web/ohjelmoitava-web/implementing-rest-apis-with-flask/#dynamic-schemas-static-methods
"""

import json

from flask import Response, request, url_for, abort
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound
from werkzeug.routing import BaseConverter

from inventorymanager import db
from inventorymanager.models import Location
from jsonschema import validate, ValidationError


class LocationCollection(Resource):
    """Class for collection of warehouse locations including addresses. /api/Locations/"""

    def get(self):
        """Gets list of locations from database"""
        body = []
        for location in Location.query.all():
            location_json = location.serialize()
            location_json["uri"] = url_for("api.locationitem", location_id=location.location_id, _external=True)
            body.append(location_json)

        return Response(json.dumps(body), 200, mimetype='application/json')

    def post(self):
        try:
            validate(request.json, Location.get_schema())
            location = Location()
            location.deserialize(request.json)

            db.session.add(location)
            db.session.commit()

        except ValidationError as e:
            return abort(400, e.message)

        except IntegrityError:
            return abort(409, "Location already exists")

        return Response(
            status=201,
            headers={
                "Location": url_for("api.locationitem", location=location)
            }
        )


class LocationItem(Resource):
    """ Class for a location resource. '/api/Locations/location_id/' """

    def get(self, location_id):

        location = Location.query.get(location_id)
        if not location:
            return {"message": "Location not found"}, 404
        return location.serialize(), 200

    def put(self, location_id):
        """
        Updates existing location_id. Validates against JSON schema.
        :parameter location_id: integer ID of location object
        """
        if not request.is_json:
            return {'message': 'Request must be JSON'}, 415

        data = request.get_json()
        try:
            validate(instance=data, schema=Location.get_schema())
        except ValidationError as e:
            return {'message': 'Validation error', 'errors': str(e)}, 400

        location = Location.query.get(location_id)
        if not location:
            return {'message': 'Location not found'}, 404

        location.deserialize(data)

        try:
            db.session.add(location)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {'message': 'Database error', 'errors': str(e)}, 500

        return {}, 204

    def delete(self, location_id):
        """
        Deletes existing location. Returns status code 204 if deletion is successful.
        """
        db.session.delete(location_id)
        db.session.commit()
        return Response(status=204)


class LocationConverter(BaseConverter):
    """
    URLConverter for a location resource.
    to_python takes a location_id and returns a Location object.
    to_url takes a Location object and returns the corresponding location_id
    """

    def to_python(self, value):
        """
        Converts a location_id in a location object with information from database
        :parameter value: str representing the location id
        raises a NotFound error if it is impossible to convert the string in an int or if the
        location is not found.
        :return: a Location object corresponding to the location_id.
        """

        try:
            int_id = int(value)
        except ValueError as exc:
            raise NotFound from exc

        db_location = Location.query.filter_by(location_id=int_id).first()
        if db_location is None:
            raise NotFound
        return db_location

    def to_url(self, value):
        """
        Converts a location object to a value used in the URI
        :param value: Location Object
        :return: the value
        """

        return str(value.location_id)

# app.url_map.converters['db_location'] = LocationConverter


# class SensorItem(Resource):

# @cache.cached()
# def get(self, sensor):
# db_sensor = Sensor.query.filter_by(name=sensor).first()
# if db_sensor is None:
# raise NotFound
# body = {
# "name": db_sensor.name,
# "model": db_sensor.model,
# "location": db_sensor.location.description
# }
# return Response(json.dumps(body), 200, mimetype=JSON)
