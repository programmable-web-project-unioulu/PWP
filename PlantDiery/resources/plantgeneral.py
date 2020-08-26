from flask import Response, request, url_for
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from jsonschema import validate, ValidationError
from .. import db
from .. import api
from ..utils import PlantBuilder, create_error_response
from ..models import PlantGeneral
from ..constants import *
import json


class PlantGeneral(Resource):

    def get(self, plant_id):
        '''
        GET single general plant information
        uuid used as identifier
        /api/plantsgeneral/<plant_id>/
        '''
        saved_gen_plant = PlantGeneral.query.filter_by(plant_id=plant_id).first()
        if saved_gen_plant is None:
            return create_error_response(
                title="Not found",
                status_code=404,
                message="No general plant with given id saved"
            )

        body = PlantBuilder(
            uuid=saved_gen_plant.uuid,
            instruction=saved_gen_plant.instruction,
            specie=saved_gen_plant.specie
        )
        body.add_control("self",
            url_for("api.plantsgeneral", plant_id=saved_gen_plant.uuid))
        body.add_control("profile", PLANT_GENERAL_PROFILE)
        body.add_control_delete_general_plant(plant_id=saved_gen_plant.uuid)
        body.add_control_modify_general_plant(plant_id=saved_gen_plant.uuid)
        body.add_namespace("plandi", LINK_RELATIONS_URL)

        return Response(response=json.dumps(body), status=200, mimetype=MASON)

    def put(self, plant_id):
        '''
        PUT (UPDATE()) single general plant information
        uuid used as identifier
        /api/generalplants/<plant_id>/
        '''

        if not request.json:
            return create_error_response(
                415,
                "Content type error",
                "Content type must be json"
            )
        try:
            validate(request.json, PlantGeneral.get_schema())
        except ValidationError as e:
            return create_error_response(
                400,
                "Invalid JSON document",
                str(e)
            )

        saved_gen_plant = PlantGeneral.query.filter_by(plant_id=plant_id).first()

        # Plant with given name does not exists in the database
        if saved_gen_plant is None:
            return create_error_response(
                404,
                "Not found",
                "No plant with uuid {} found".format(plant_id)
            )
        # Previous checks OK, update plant item
        saved_gen_plant.uuid=request.json["uuid"]
        saved_gen_plant.instruction=request.json["instruction"]
        saved_gen_plant.specie=request.json["specie"]

        db.session.commit()

        return Response(status=204, mimetype=MASON)


class PlantGeneralCollection(Resource):
    def get(self):
        '''
        Get General Plant Collection Resource
        '''
        gen_plants = PlantGeneral.query.all()
        if gen_plants is None:
            return create_error_response(
            404,
            "Not found",
            "Database is empty"
            )

        body = PlantBuilder(items=[])
        for plant in gen_plants:
            plantItem = PlantBuilder(
                name=plant.name,
                instruction=plant.instruction,
                specie=plant.specie
            )
            plantItem.add_control("self",
                url_for("api.plantgeneral", uuid=plant.uuid))
            plantItem.add_control("profile", PLANT_GENERAL_PROFILE)
            body["items"].append(plantItem)
        body.add_namespace("plandi", LINK_RELATIONS_URL)
        body.add_control_add_general_plant()
        return Response(json.dumps(body), 200, mimetype=MASON)

    def post(self):
        if not request.json:
            return create_error_response(
            415,
            "Wrong content type",
            "content type not json"
        )

        try:
            validate(request.json, PlantGeneral.get_schema())
        except ValidationError as e:
            return create_error_response(
                400,
                "Invalid json document",
                str(e)
            )

        gen_plant = PlantGeneral(
            uuid = request.json["uuid"],
            instruction = request.json["instruction"],
            specie=request.json["specie"]
        )
        try:
            db.session.add(gen_plant)
            db.session.commit()
        except IntegrityError:
            return create_error_response(
                409,
                "Already exists",
                "Plant with uuid {} already exists".format(
                request.json["uuid"])
            )

        return Response(status=201, headers={"Location": url_for(
            api.plantgeneral, uuid=request.json["uuid"]
        )}, mimetype=MASON)
