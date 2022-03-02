from flask_restful import Resource

import api

db = api.db

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