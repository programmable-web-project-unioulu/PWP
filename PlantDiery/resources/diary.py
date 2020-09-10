from flask import Response, request, url_for
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from jsonschema import validate, ValidationError
from .. import db
from .. import api
from ..utils import PlantBuilder, create_error_response
from ..models import Diary
from ..constants import *
import json


class DiaryEntry(Resource):
    def get(self, entry_id):
        '''
        GET single diary entry
        /api/plantdiary/<entry_id>/
        '''
        saved_entry = Diary.query.filter_by(uuid=entry_id).first()
        if saved_entry is None:
            return create_error_response(
                status_code=404,
                title="Not found",
                message="No diary entry id {}".format(entry_id)
            )

        body = PlantBuilder(
            uuid=saved_entry.uuid,
            date=saved_entry.date,
            description=saved_entry.description,
            plant=saved_entry.plant
        )

        body.add_control("self", url_for("api.diaryentry", entry_id=entry_id))
        body.add_control("profile", DIARY_PROFILE)
        body.add_control_delete_diary_entry(entry_id=entry_id)
        body.add_namespace("plandi", LINK_RELATIONS_URL)

        return Response(response=json.dumps(body), status=200, mimetype=MASON)

    def delete(self, entry_id):
        '''
        DELETE selected diary entry
        /api/plantdiary/<entry_id>/
        '''
        saved_entry = Diary.query.filter_by(uuid=entry_id).first()
        if saved_entry is None:
            return create_error_response(
                404,
                "Not found",
                "No entry with id {} found".format(entry_id)
            )
        
        db.session.delete(saved_entry)
        db.session.commit()

        return Response(status=204, mimetype=MASON)

class DiaryCollection(Resource):
    def get(self):
        '''
        GET all diary entries
        /api/plantdiary/
        '''
        entries = Diary.query.all()
        if entries is None:
            return create_error_response(
                404,
                "Not found",
                "Database is empty"
            )
        body = PlantBuilder(items=[])
        for entry in entries:
            diaryItem = PlantBuilder(
                uuid=entry.uuid,
                date=entry.date,
                description=entry.description,
                plant=entry.plant
            )
            diaryItem.add_control("self", url_for("api.diaryentry", entry_id=entry.uuid))
            diaryItem.add_control("profile", DIARY_PROFILE)
            body["items"].append(diaryItem)
        body.add_namespace("plandi", LINK_RELATIONS_URL)
        body.add_control_add_diary_entry()

        return Response(json.dumps(body), 200, mimetype=MASON)

    def post(self):
        '''
        POST new diary entry
        /api/plantdiary/
        '''
        if not request.json:
            return create_error_response(
                415,
                "Wrong content type",
                "content type not json"
            )
            
        try:
            validate(request.json, Diary.get_schema())
        except ValidationError as e:
            return create_error_response(
                400,
                "Invalid json document",
                str(e)
            )

        entry = Diary(
            uuid=request.json["uuid"],
            date=request.json["date"],
            description=request.json["description"],
            plant=request.json["plant"]
        )

        try:
            db.session.add(entry)
            db.session.commit()
        except:
            return create_error_response(
                409,
                "Already exists",
                "Diary entry with id {} already exists".format(request.json["uuid"])
            )

        return Response(
            status=201,
            mimetype=MASON,
            headers={"Location": url_for("api.diaryentry", entry_id=request.json["uuid"])}
        )


