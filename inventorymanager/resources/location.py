"""
Code edited from course example
https://github.com/enkwolf/pwp-course-sensorhub-api-example/blob/master/sensorhub/resources/location.py
Examples from PWP course exercise 2
https://lovelace.oulu.fi/ohjelmoitava-web/ohjelmoitava-web/implementing-rest-apis-with-flask/#dynamic-schemas-static-methods
"""


import json
from jsonschema import validate, ValidationError
from flask import Response, request, url_for, abort
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound
from werkzeug.routing import BaseConverter

from inventorymanager import db
from inventorymanager.models import Location


class LocationCollection(Resource):
    """Class for collection of warehouse locations including addresses. /api/Locations/"""

    def get(self):
        """Gets list of locations from database"""

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

    def post(self): #should this be PUT instead?
        data = request.get_json(force=True)

        try:
            validate(instance=data, schema=Location.get_schema())
        except ValidationError as e:
            return {'message': 'Validation error', 'errors': str(e)}, 400

        new_location = Location()
        new_location.deserialize(data)

        db.session.add(new_location)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {'message': 'Database error', 'errors': str(e)}, 500

        return jsonify({
            'message': 'Location created successfully',
            'location': new_location.serialize(),
            'links': {
                'self': url_for('api.locationitem', location_id=new_location.location_id, _external=True)
            }
        }), 201

    def delete(self, location):
        """
        Deletes existing location. Returns status code 204 if deletion is successful.
        """
        db.session.delete(location)
        db.session.commit()
        return Response(status=204)

class LocationConverter(BaseConverter):
    """
    URLConverter for a location resource.
    to_python takes a location_id and returns a Location object.
    to_url takes a Location object and returns the corresponding location_id
    """

    def to_python(self, location_id):
        """Converts a location_id in a location object """

        try:
            int_id = int(value)
        except ValueError as exc:
            raise NotFound from exc

        db_location = Location.query.filter_by(location_id=int_id).first()
        if db_location is None:
            raise NotFound
        return db_location

    def to_url(self, db_location):
        """Converts a location object to a location_id """

        return db_location.name



app.url_map.converters['db_location'] = ProductConverter

    








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