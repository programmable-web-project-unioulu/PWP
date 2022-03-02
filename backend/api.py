import enum
from flask import Flask, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine

# Import necessary classes so we can use it to add the resources later
import category_endpoints
import movie_endpoints
import review_endpoints
import user_endpoints

# Establish a database connection and initialize API object
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-review.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)
db = SQLAlchemy(app)

# Enable foreign key constraints for SQLite
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
	cursor = dbapi_connection.cursor()
	cursor.execute("PRAGMA foreign_keys=ON")
	cursor.close()

class UserType(enum.Enum):
	admin = "Admin"
	basicUser = "Basic User"

class Movie(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String, nullable=False)
	director = db.Column(db.String, nullable=False)
	length = db.Column(db.Integer, nullable=False)
	release_date = db.Column(db.Date, nullable=False)
	category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="RESTRICT"), nullable=False)

	category = db.relationship("Category")
	reviews = db.relationship("Review", back_populates="movie")


class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String, nullable=False)

	movies = db.relationship("Movie", back_populates="category")


class Review(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	rating = db.Column(db.Integer, nullable=False)
	comment = db.Column(db.Text, nullable=False)
	date = db.Column(db.Date, nullable=False)
	author_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="SET NULL"), nullable=True)
	movie_id = db.Column(db.Integer, db.ForeignKey("movie.id", ondelete="CASCADE"), nullable=False)

	movie = db.relationship("Movie")
	user = db.relationship("User")


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String, nullable=False, unique=True)
	emailAddress = db.Column(db.String, nullable=False, unique=True)
	password = db.Column(db.String, nullable=False)
	role = db.Column(db.Enum(UserType), nullable=False)

	review = db.relationship("Review", back_populates="user")

# Add the endpoints for categories
api.add_resource(category_endpoints.CategoryCollection, "/api/categories/")
api.add_resource(category_endpoints.CategoryItem, "/api/categories/<category_id>/")

# Add the endpoints for movies
api.add_resource(movie_endpoints.MovieCollection, "/api/movies/")
api.add_resource(movie_endpoints.MovieItem, "/api/movies/<movie_id>/")

# Add the endpoints for reviews
api.add_resource(review_endpoints.MovieReviewCollection, "/api/movies/<movie_id>/reviews/")
api.add_resource(review_endpoints.MovieReviewItem, "/api/movies/<movie_id>/reviews/<review_id]>")

# Add the endpoints for users
api.add_resource(user_endpoints.UserCollection, "/api/users/")
api.add_resource(user_endpoints.UserItem, "/api/users/<user_id>/")
api.add_resource(user_endpoints.UserReviewCollection, "/api/users/<user_id>/reviews/")
