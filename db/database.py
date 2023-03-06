from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import Engine
from sqlalchemy import event

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
app.app_context().push()


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    
    # creates a connection from Group -> Breed
    breeds = db.relationship("Breed", back_populates="group")
    def serialize(self):
        return {
            "name": self.name,
            "id": self.id
        }
    
    def deserialize(self, doc):
        self.name = doc["name"]

    @staticmethod
    def json_schema():
        schema = {
            "type": "object",
            "required": ["name"]
        }
        props = schema["properties"] = {}
        props["name"] = {
            "description": "Group's unique name",
            "type": "string"
        }
        return schema

class Characteristics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    life_span = db.Column(db.Integer, db.CheckConstraint('life_span>5'),
                    db.CheckConstraint('life_span<25'), nullable=False)
    coat_length = db.Column(db.Float, db.CheckConstraint('coat_length<1'), nullable=True)
    exercise = db.Column(db.Float, db.CheckConstraint('exercise>0'),
                    db.CheckConstraint('exercise<5'), nullable=True)
    
    in_breed = db.relationship("Breed", back_populates="characteristics")

    def serialize(self):
        return {
            "breed": [breed.name for breed in self.in_breed],
            "char_id": self.id,
            "coat_length": self.coat_length,
            "life_span": self.life_span,
            "exercise": self.exercise,
        }
    
    @staticmethod
    def json_schema():
        schema = {
            "type": "object",
            "required": ["in_breed", "life_span"]
        }
        props = schema["properties"] = {}
        props["in_breed"] = {
            "description": "Breed that the characteristics describe",
            "type": "string"
        }
        props["life_span"] = {
            "description": "Lifespan of a breed",
            "type": "number"
        }
        return schema

class Facts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fact = db.Column(db.String(128), nullable=False)
    
    # creates a connection from Facts -> Breed
    breed_id = db.Column(db.Integer, db.ForeignKey("breed.id"), ondelete="SET NULL")
    breed = db.relationship("Breed", back_populates="facts")

    def serialize(self):
        return {
            "fact": self.fact,
            "breed": self.breed.serialize(),
            "id": self.id
        }
    
    @staticmethod
    def json_schema():
        schema = {
            "type": "object",
            "required": ["fact", "breed"]
        }
        props = schema["properties"] = {}
        props["fact"] = {
            "description": "Fact about a breed",
            "type": "string"
        }
        props["breed"] = {
            "description": "Breed regarding the fact",
            "type": "string"
        }
        return schema

class Breed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    char_id = db.Column(db.Integer, db.ForeignKey("characteristics.id"), ondelete="SET NULL")
    
    # creates a connection from Breed -> Group
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"), ondelete="SET NULL")
    group = db.relationship("Group", back_populates="breeds")
    
    # creates a connection from Breed -> Characteristics
    characteristics = db.relationship("Characteristics", back_populates="in_breed", uselist=False)
    
    # creates a connection from Breed -> Facts
    facts = db.relationship("Facts", back_populates="breed")

    def serialize(self, short_form=False):
        doc = {
            "name": self.name,
            "id": self.id
        }
        if not short_form:
            doc["group"] = self.group.serialize()
            doc["facts"] = [fact.fact for fact in self.facts]
            if self.characteristics:
                doc["characteristics"] = {"char_id": self.characteristics.id,
                                        "life_span": self.characteristics.life_span,
                                        "coat_length": self.characteristics.coat_length,
                                        "exercise": self.characteristics.exercise}
        return doc
    
    def deserialize(self, doc):
        self.name = doc["name"]
        #self.group = doc["group"]
    
    @staticmethod
    def json_schema():
        schema = {
            "type": "object",
            "required": ["name", "group"]
        }
        props = schema["properties"] = {}
        props["name"] = {
            "description": "Breeds unique name",
            "type": "string"
        }
        props["group"] = {
            "description": "Name of the breed's group",
            "type": "string"
        }
        return schema


db.create_all()