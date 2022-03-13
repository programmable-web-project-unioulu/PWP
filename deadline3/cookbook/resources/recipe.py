import json
from sqlite3 import IntegrityError
from flask import url_for, Response, request
from flask_restful import Api, Resource
from cookbook.models import Recipe
from .. import db
from ..utils import RecipeBuilder, create_error_response
from ..constants import *
from werkzeug.exceptions import NotFound
from werkzeug.routing import BaseConverter
from jsonschema import validate, ValidationError, draft7_format_checker


class RecipeCollection(Resource):

    def get(self, user):
        build = RecipeBuilder(items=[])
        inventory = db.session.query(Recipe).all()
        for item in inventory:
            data = RecipeBuilder(
                name=item.name,
                description=item.description,
                difficulty=item.difficulty,
                owner=user.name,
                user_id=item.user_id,

            )
            data.add_control("self", url_for("api.recipeitem", user=user.name, recipe=item.name))
            build["items"].append(data)
        build.add_control("self", href=url_for("api.recipecollection", user=user.name))
        build.add_control_add_recipe(user.name)

        return Response(
            status=200,
            response=json.dumps(build, indent=4, separators=(',', ': '), sort_keys=True),
            mimetype=MASON)

    def post(self, user):
        if request.json == None:
            return create_error_response(415, "BAD CONTENT", "MUST BE JSON")
        try:
            validate(
                request.json,
                Recipe.json_schema(),
                format_checker=draft7_format_checker
            )
        except ValidationError as e:
            return create_error_response(
                400,
                "Invalid JSON",
                str(e))
        try:
            p_name = request.json["name"]
            recipe_name = Recipe.query.filter_by(name=p_name).first()
            if recipe_name:
                return create_error_response(409, "ON JO", "Duplicate 🥝")
            p_desc = request.json["description"]
            if not isinstance(p_desc, str):
                return create_error_response(400, "Invalid values")
        except KeyError:
            return create_error_response(400, "KeyError")
        try:
            new_recipe = Recipe(
            name=p_name,
            description=p_desc,
            )
            db.session.add(new_recipe)
            db.session.commit()
        except IntegrityError:
            return create_error_response(409, "Duplicate", "Database error")

        return Response(
            status=201,
            mimetype=MASON,
            headers={"Location": url_for("api.recipeitem", user=user.name, recipe=p_name)}
        )

class RecipeItem(Resource):
    
    def get(self, recipe, user):
        recipe_item = db.session.query(Recipe).filter_by(name=recipe.name).first()
        if recipe_item == None:
            return create_error_response(404, "Ei oo", "No recipe_item")
        data = RecipeBuilder(
            name=recipe_item.name,
            description=recipe_item.description
        )
        data.add_control("self", url_for("api.recipeitem", user=user.name, recipe=recipe.name))
        data.add_control("collection", url_for("api.recipecollection", user=user.name))
        data.add_control_edit_recipe(recipe, user)
        data.add_control_delete_recipe(recipe, user)

        return Response(json.dumps(data), status=200, mimetype=JSON)
    
    def put(self, recipe):
        recipe_item = db.session.query(Recipe).filter_by(name=recipe.name).first()
        if not recipe_item:
            return create_error_response(404, "recipe not found")
        try:
            recipe_item.name = request.json["name"]
            recipe_item.description = request.json["description"]
        except TypeError:
            return create_error_response(415, "Wrong content", "Should be JSON")
        except KeyError:
            return create_error_response(400, "Invalid content", "Validation fails")
        
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return create_error_response(status_code=409, title="Taken")
        return Response(status=204, mimetype=MASON)
    
    def delete(self, recipe):
        recipe_h = db.session.query(Recipe).filter_by(name=recipe.name).first()
        if not recipe_h:
            return create_error_response(404, "Not Found", "recipe not found")
        
        db.session.delete(recipe_h)
        db.session.commit()
        return Response(status=204, mimetype=MASON)

class RecipeConverter(BaseConverter):
    def to_python(self, recipe):
        db_recipe = db.session.query(Recipe).filter_by(name=recipe).first()
        if db_recipe is None:
            raise NotFound
        return db_recipe
    
    def to_url(self, db_recipe):
        return str(db_recipe)