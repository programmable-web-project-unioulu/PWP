from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_restful import Resource
from sqlalchemy import event
from sqlalchemy.engine import Engine

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
	cursor = dbapi_connection.cursor()
	cursor.execute("PRAGMA foreign_keys=ON")
	cursor.close()

api = Api(app)

from MovieReview.backend.database.database import User, Movie, Category, Review

class UserCollection(Resource):
	def get(self):
		"""
		---
		description: Get the list of all users
		responses:
			'200':
				description: List of users
				content:
					application/json:
						example:
						- username: test-user-1
						  email_address: test-user-1@oulu.fi
						  password: 1e234d
						  role: BasicUser
              			- username: test-user-2
              			  email_address: test-user-2@oulu.fi
              			  password: 544f8
              			  role: Admin
		"""
		users = User.query.all()
		res = User.serialize_list(users)
		return res

	def post(self):
		abc = 'd'

api.add_resource(UserCollection, "/api/users/")

class UserItem(Resource):
	def get(self):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def put(self, user_id):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def delete(self, user_id):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

api.add_resource(UserItem, "/api/users/<user_id>/")

class UserReviewCollection(Resource):
	def get(self, user_id):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

api.add_resource(UserReviewCollection, "/api/users/<user_id>/reviews/")

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

api.add_resource(MovieCollection, "/api/movies/")

class MovieItem(Resource):
	def get(self, movie_id):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def put(self, movie_id):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def delete(self, movie_id):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

api.add_resource(MovieItem, "/api/movies/<movie_id>/")

class MovieReviewCollection(Resource):
	def get(self, movie_id):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def post(self, movie_id):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

api.add_resource(MovieReviewCollection, "/api/movies/<movie_id>/reviews/")

class MovieReviewItem(Resource):
	def get(self, movie_id, review_id):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def put(self, movie_id, review_id):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def delete(self, movie_id, review_id):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

api.add_resource(MovieReviewItem, "/api/movies/<movie_id>/reviews/<review_id]>")

class CategoryCollection(Resource):
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

api.add_resource(CategoryCollection, "/api/categories/")

class CategoryItem(Resource):
	def get(self, category_id):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def put(self, category_id:
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

	def delete(self, category_id):
		"""
		---
		description:
		responses:
			'200':
		"""
		abc = 'd'

api.add_resource(MovieReviewItem, "/api/categories/<category_id>/")
