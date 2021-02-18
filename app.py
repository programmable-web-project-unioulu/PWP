from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'your_database',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

"""
example
class User(db.Document):
    name = db.StringField()
    email = db.StringField()
    def to_json(self):
        return {"name": self.name,
                "email": self.email}
"""

class Material(db.Document):
    structure_name = db.StringField(required = True, max_length = 50)

class Material_Volume(db.Document):
    size_a = db.FloatField()        #or size_a = db.FloatField(0.0001, 20)
    size_b = db.FloatField()
    size_c = db.FloatField()

class Material_other(db.Document):
    bonding_length = db.FloatField(required = True)    #between 0.0001-5

class Material_Fermi(db.Document):
    fermi = 1.0        #was this calculated

class Material_Structure_type(db.Document):
    structure_type = db.StringField(required = True, max_length = 50)
    dimension_type = db.StringField(required = True, max_length = 64)

if __name__ == "__main__":
    app.run(debug=True)