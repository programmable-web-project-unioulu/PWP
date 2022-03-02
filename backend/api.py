import enum
from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine
from jsonschema import validate, ValidationError, draft7_format_checker
from werkzeug.exceptions import NotFound
from werkzeug.routing import BaseConverter
import datetime

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
		return [self.id, self.title, self.director, self.length, self.release_date, self.category]

	def deserialize(self, doc):
		self.title = doc["title"]
		self.director = doc.get("director")
		self.length = doc.get("length")
		self.release_date = datetime.fromisoformat(doc["release_date"])
		self.category_id = doc.get("category_id")


class Category(db.Model, Serializer):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String, nullable=False)

	movies = db.relationship("Movie", back_populates="category")

	def serialize(self):
		return [self.id, self.title]

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
		self.date = datetime.fromisoformat(doc["date"])
		self.author_id = doc.get("author_id")
		self.movie_id = doc.get("movie_id")

	def serialize(self):
		return [self.id, self.rating, self.comment, self.date, self.author_id, self.movie_id]


class User(db.Model, Serializer):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String, nullable=False, unique=True)
	email_address = db.Column(db.String, nullable=False, unique=True)
	password = db.Column(db.String, nullable=False)
	role = db.Column(db.Enum(UserType), nullable=False)

	review = db.relationship("Review", back_populates="user")

	def serialize(self):
		return [self.id, self.username, self.email_address, self.password, self.role]

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
		return db_category.id


class MovieConverter(BaseConverter):
	def to_python(self, movie_id):
		db_movie = Category.query.filter_by(id=movie_id).first()
		if db_movie is None:
			raise NotFound
		return db_movie

	def to_url(self, db_movie):
		return db_movie.id


class ReviewConverter(BaseConverter):
	def to_python(self, review_id):
		db_review = Category.query.filter_by(id=review_id).first()
		if db_review is None:
			raise NotFound
		return db_review

	def to_url(self, db_review):
		return db_review.id


class UserConverter(BaseConverter):
	def to_python(self, user_id):
		db_user = Category.query.filter_by(id=user_id).first()
		if db_user is None:
			raise NotFound
		return db_user

	def to_url(self, db_user):
		return db_user.id


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
			return str(e), 400

		category = Category()
		category.deserialize(request.json)

		db.session.add(category)
		db.session.commit()

		return 201


api.add_resource(CategoryCollection, "/api/categories/")


class CategoryItem(Resource):
	def get(self, category):
		abc = 'd'

	def put(self, category):
		abc = 'd'

	def delete(self, category):
		abc = 'd'


api.add_resource(CategoryItem, "/api/categories/<category_id>/")


# MOVIE LOGIC
class MovieCollection(Resource):
	def get(self):
		abc = 'd'

	def post(self):
		abc = 'd'
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
