from flask import request
from flask_restful import Resource
from jsonschema import validate, ValidationError, draft7_format_checker

import api

db = api.db

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