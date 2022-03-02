from flask_restful import Resource

from MovieReview.backend.database.database import db
from MovieReview.backend.database.database import Movie

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
