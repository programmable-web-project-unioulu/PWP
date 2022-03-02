import enum
from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine

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


# CATEGORY LOGIC
class CategoryCollection(Resource):
	def get(self):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def post(self, category):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

class CategoryItem(Resource):
	def get(self, category):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def put(self, category):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def delete(self, category):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

api.add_resource(CategoryCollection, "/api/categories/")
api.add_resource(CategoryItem, "/api/categories/<category_id>/")


# MOVIE LOGIC
class MovieCollection(Resource):
	def get(self):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def post(self):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

class MovieItem(Resource):
	def get(self, movie):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def put(self, movie):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def delete(self, movie):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

api.add_resource(MovieCollection, "/api/movies/")
api.add_resource(MovieItem, "/api/movies/<movie_id>/")


# REVIEW LOGIC
class MovieReviewCollection(Resource):
	def get(self, movie):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def post(self, movie):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

class MovieReviewItem(Resource):
	def get(self, movie, review):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def put(self, movie, review):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def delete(self, movie, review):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

api.add_resource(MovieReviewCollection, "/api/movies/<movie_id>/reviews/")
api.add_resource(MovieReviewItem, "/api/movies/<movie_id>/reviews/<review_id>")

# USERS LOGIC
class UserCollection(Resource):
	def get(self):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def post(self):
		abc = 'd'

class UserItem(Resource):
	def get(self, user):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def put(self, user):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def delete(self, user):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

class UserReviewCollection(Resource):
	def get(self, user):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

api.add_resource(UserCollection, "/api/users/")
api.add_resource(UserItem, "/api/users/<user_id>/")
api.add_resource(UserReviewCollection, "/api/users/<user_id>/reviews/")
