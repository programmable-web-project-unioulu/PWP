import enum

from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine
from jsonschema import validate, ValidationError, draft7_format_checker
from werkzeug.exceptions import NotFound
from sqlalchemy import exc
from werkzeug.routing import BaseConverter
from datetime import date

from helper.serializer import Serializer

# Establish a database connection and initialize API + DB object
from json_schemas.category_json_schema import get_category_json_schema
from json_schemas.movie_json_schema import get_movie_json_schema
from json_schemas.user_json_schema import get_user_json_schema
from json_schemas.review_json_schema import get_review_json_schema

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-review.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.url_map.strict_slashes = False

api = Api(app)
db = SQLAlchemy(app)

# Enable foreign key constraints for SQLite
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
	cursor = dbapi_connection.cursor()
	cursor.execute("PRAGMA foreign_keys=ON")
	cursor.execute("PRAGMA foreign_keys=ON")
	cursor.close()


# DATABASE MODEL
class UserType(enum.Enum):
	admin = "Admin"
	basicUser = "Basic User"


class Movie(db.Model, Serializer):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String, nullable=False)
	director = db.Column(db.String, nullable=False)
	length = db.Column(db.Integer, nullable=False)
	release_date = db.Column(db.Date, nullable=False)
	category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="RESTRICT"), nullable=False)

	category = db.relationship("Category")
	reviews = db.relationship("Review", back_populates="movie")

	def serialize(self):
		return {
			"id": self.id,
			"title": self.title,
			"director": self.director,
			"length": self.length,
			"release_date": self.release_date.isoformat(),
			"category_id": self.category_id
		}

	def deserialize(self, doc):
		self.title = doc["title"]
		self.director = doc.get("director")
		self.length = doc.get("length")
		self.release_date = date.fromisoformat(doc["release_date"])
		self.category_id = doc.get("category_id")


class Category(db.Model, Serializer):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String, nullable=False)

	movies = db.relationship("Movie", back_populates="category")

	def serialize(self):
		return {
			"id": self.id,
			"title": self.title
		}

	def deserialize(self, doc):
		self.title = doc["title"]


class Review(db.Model, Serializer):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	rating = db.Column(db.Integer, nullable=False)
	comment = db.Column(db.Text, nullable=False)
	date = db.Column(db.Date, nullable=False)
	author_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="SET NULL"), nullable=True)
	movie_id = db.Column(db.Integer, db.ForeignKey("movie.id", ondelete="CASCADE"), nullable=False)

	movie = db.relationship("Movie")
	user = db.relationship("User")

	def deserialize(self, doc):
		self.rating = doc["rating"]
		self.comment = doc.get("comment")
		self.date = date.fromisoformat(doc["date"])
		self.author_id = doc.get("author_id")
		self.movie_id = doc.get("movie_id")

	def serialize(self):
		return {
			"id": self.id,
			"rating": self.rating,
			"comment": self.comment,
			"date": self.date.isoformat(),
			"author_id": self.author_id,
			"movie_id": self.movie_id
		}


class User(db.Model, Serializer):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String, nullable=False, unique=True)
	email_address = db.Column(db.String, nullable=False, unique=True)
	password = db.Column(db.String, nullable=False)
	role = db.Column(db.Enum(UserType), nullable=False)

	review = db.relationship("Review", back_populates="user")

	def serialize(self):
		return {
			"id": self.id,
			"username": self.username,
			"email_address": self.email_address,
			"password": self.password,
			"role": self.role
		}

	def deserialize(self, doc):
		self.username = doc["username"]
		self.email_address = doc.get("email_address")
		self.password = doc.get("password")
		self.role = doc.get("role")


# CONVERTERS
class CategoryConverter(BaseConverter):
	def to_python(self, category_id):
		db_category = Category.query.filter_by(id=category_id).first()
		if db_category is None:
			raise NotFound
		return db_category

	def to_url(self, db_category):
		return str(db_category.id)


class MovieConverter(BaseConverter):
	def to_python(self, movie_id):
		db_movie = Category.query.filter_by(id=movie_id).first()
		if db_movie is None:
			raise NotFound
		return db_movie

	def to_url(self, db_movie):
		return str(db_movie.id)


class ReviewConverter(BaseConverter):
	def to_python(self, review_id):
		db_review = Category.query.filter_by(id=review_id).first()
		if db_review is None:
			raise NotFound
		return db_review

	def to_url(self, db_review):
		return str(db_review.id)


class UserConverter(BaseConverter):
	def to_python(self, user_id):
		db_user = Category.query.filter_by(id=user_id).first()
		if db_user is None:
			raise NotFound
		return db_user

	def to_url(self, db_user):
		return str(db_user.id)


# CATEGORY LOGIC
class CategoryCollection(Resource):
	def get(self):
		categories = Category.query.all()
		categories = Category.serialize_list(categories)
		return categories, 200

	def post(self):
		if not request.json:
			return "Unsupported media type", 415

		try:
			validate(request.json, get_category_json_schema(), format_checker=draft7_format_checker)
		except ValidationError as e:
			return e.message, 400

		category = Category()
		category.deserialize(request.json)

		db.session.add(category)
		db.session.commit()

		return 201


api.add_resource(CategoryCollection, "/api/categories/")


class CategoryItem(Resource):
	def get(self, category):
		return category.serialize()

	def put(self, category):
		if not request.json:
			return "Unsupported media type", 415

		try:
			validate(request.json, get_category_json_schema(), format_checker=draft7_format_checker)
		except ValidationError as e:
			return e.message, 400

		update_category = Category()
		update_category.deserialize(request.json)

		category.title = update_category.title

		db.session.commit()

		return 204

	def delete(self, category):
		try:
			db.session.delete(category)
			db.session.commit()
			return 204
		except exc.IntegrityError as e:
			return str(e.orig), 409


app.url_map.converters["category"] = CategoryConverter
api.add_resource(CategoryItem, "/api/categories/<category:category>/")


# MOVIE LOGIC
class MovieCollection(Resource):
	def get(self):
		movies = Movie.query.all()
		movies = Category.serialize_list(movies)
		return movies, 200

	def post(self):
		if not request.json:
			return "Unsupported media type", 415

		try:
			validate(request.json, get_movie_json_schema(), format_checker=draft7_format_checker)
		except ValidationError as e:
			return e.message, 400

		movie = Movie()
		movie.deserialize(request.json)

		db.session.add(movie)
		db.session.commit()

		return 201


api.add_resource(MovieCollection, "/api/movies/")

class MovieItem(Resource):
	def get(self, movie):
		abc = 'd'

	def put(self, movie):
		abc = 'd'

	def delete(self, movie):
		abc = 'd'
api.add_resource(MovieItem, "/api/movies/<movie_id>/")


# REVIEW LOGIC
class MovieReviewCollection(Resource):
	def get(self):
		abc = 'd'

	def post(self):
		abc = 'd'
api.add_resource(MovieReviewCollection, "/api/movies/<movie_id>/reviews/")

class MovieReviewItem(Resource):
	def get(self, movie, review):
		abc = 'd'

	def put(self, movie, review):
		abc = 'd'

	def delete(self, movie, review):
		abc = 'd'
api.add_resource(MovieReviewItem, "/api/movies/<movie_id>/reviews/<review_id>")


# USERS LOGIC
class UserCollection(Resource):
	def get(self):
		abc = 'd'

	def post(self):
		abc = 'd'
api.add_resource(UserCollection, "/api/users/")

class UserItem(Resource):
	def get(self, user):
		abc = 'd'

	def put(self, user):
		abc = 'd'

	def delete(self, user):
		abc = 'd'
api.add_resource(UserItem, "/api/users/<user_id>/")

class UserReviewCollection(Resource):
	def get(self, user):
		abc = 'd'
api.add_resource(UserReviewCollection, "/api/users/<user_id>/reviews/")
