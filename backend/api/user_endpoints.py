from flask_restful import Resource

from MovieReview.backend.database.database import db
from MovieReview.backend.database.database import User

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