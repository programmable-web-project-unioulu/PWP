from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask import Flask, request


db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cookbook.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():

        from . import models
        from .api_routes import recipe_route, populate_route, ingredient_route, user_route, recipe_ingredients

        db.create_all()  # Create database tables for our data models

        api = Api(app)

        api.add_resource(recipe_route.Recipes, "/api/recipes")
        api.add_resource(populate_route.Populate, "/api/populate")
        api.add_resource(ingredient_route.Ingredients, "/api/ingredients")
        api.add_resource(user_route.UserCollection, "/api/users")
        api.add_resource(recipe_ingredients.Recipeingredients, "/api/recipeingredients")

        return app
