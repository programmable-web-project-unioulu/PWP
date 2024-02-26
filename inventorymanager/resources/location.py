
"""Code edited from course example 
https://github.com/enkwolf/pwp-course-sensorhub-api-example/blob/master/sensorhub/resources/location.py"""


import json
from jsonschema import validate, ValidationError
from flask import Response, request, url_for, abort
from flask_restful import Resource
from inventorymanager import db
from inventorymanager.models import Location
#from inventorymanager.constants import *
#from inventorymanager.utils import SensorhubBuilder, create_error_response


class LocationCollection(Resource):

    def get(self):
        locations = Location.query.all()
        return [location.serialize() for location in locations], 200

    def post(self):
        # Implementation for creating a new location
        pass


class LocationItem(Resource):

    def get(self, location_id):
        location = Location.query.get(location_id)
        if not location:
            return {"message": "Location not found"}, 404
        return location.serialize(), 200

    def post(self, location):
        def post(self):
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



    
  