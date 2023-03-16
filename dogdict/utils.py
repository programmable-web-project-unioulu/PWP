from flask import Response
from dogdict.models import Breed, Facts, Group
from werkzeug.exceptions import NotFound
from werkzeug.routing import BaseConverter
"""
Converters
"""

class GroupConverter(BaseConverter):

    def to_python(self, value):
        value = value.capitalize()  # add capitalization so URI does not need to be uppercase
        print(value)
        db_group = Group.query.filter_by(name=value).first()
        if db_group is None:
            raise NotFound
        return db_group

    def to_url(self, value):
        # THESE NEED TO BE IMPLEMENTED
        print("BREED:", value)
        return str(value)


class BreedConverter(BaseConverter):

    def to_python(self, value):  # MARTTI MUUTTI TÄMÄN ID:LLÄ TOIMIVAKSI, MIETITÄÄN MITÄ TAPAHTUU
        print(value)
        db_breed = Breed.query.filter_by(id=value).first()
        if db_breed is None:
            return Response(status=404)
        return db_breed

    def to_url(self, value):
        # THESE NEED TO BE IMPLEMENTED
        print("BREED:", value)
        return str(value)


class FactConverter(BaseConverter):
    def to_python(self, value):
        db_fact = Facts.query.filter_by(id=value).first()
        if db_fact is None:

            return Response(status=404)
        return db_fact

    def to_url(self, value):
        # THESE NEED TO BE IMPLEMENTED
        print("fact:", value)
        return str(value)