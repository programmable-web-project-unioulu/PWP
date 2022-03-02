from flask import Flask, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine

# Import necessary classes so we can use it to add the resources later
from category_endpoints import CategoryCollection, CategoryItem
from movie_endpoints import MovieCollection, MovieItem
from review_endpoints import MovieReviewCollection, MovieReviewItem
from user_endpoints import UserCollection, UserItem, UserReviewCollection

# Establish a database connection and initialize API object
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-review.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)

# Enable foreign key constraints for SQLite
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
	cursor = dbapi_connection.cursor()
	cursor.execute("PRAGMA foreign_keys=ON")
	cursor.close()

# Add the endpoints for categories
api.add_resource(CategoryCollection, "/api/categories/")
api.add_resource(CategoryItem, "/api/categories/<category_id>/")

# Add the endpoints for movies
api.add_resource(MovieCollection, "/api/movies/")
api.add_resource(MovieItem, "/api/movies/<movie_id>/")

# Add the endpoints for reviews
api.add_resource(MovieReviewCollection, "/api/movies/<movie_id>/reviews/")
api.add_resource(MovieReviewItem, "/api/movies/<movie_id>/reviews/<review_id]>")

# Add the endpoints for users
api.add_resource(UserCollection, "/api/users/")
api.add_resource(UserItem, "/api/users/<user_id>/")
api.add_resource(UserReviewCollection, "/api/users/<user_id>/reviews/")
