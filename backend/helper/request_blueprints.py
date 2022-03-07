from jsonschema import validate, ValidationError, draft7_format_checker
from sqlalchemy import exc


def post_blueprint(request, json_schema, db, create_object):
    if not request.json:
        return "Unsupported media type", 415

    try:
        validate(request.json, json_schema(), format_checker=draft7_format_checker)
    except ValidationError as e:
        return e.message, 400

    created_object = create_object()

    try:
        db.session.add(created_object)
        db.session.commit()
        return 201
    except exc.IntegrityError as e:
        return str(e.orig), 409


def put_blueprint(request, json_schema, db, update_object):
    if not request.json:
        return "Unsupported media type", 415

    try:
        validate(request.json, json_schema(), format_checker=draft7_format_checker)
    except ValidationError as e:
        return e.message, 400

    update_object()

    try:
        db.session.commit()
    except exc.IntegrityError as e:
        return str(e.orig), 409

    return 204
