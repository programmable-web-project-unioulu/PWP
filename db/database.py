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
    breed_id = db.Column(db.Integer, db.ForeignKey("breed.id"))

    # creates a connection from Breed -> Group
    breed = db.relationship("Breed", back_populates="in_group")


class Characteristics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    life_span = db.Column(db.String(64), nullable=False)
    coat_length = db.Column(db.String(64), nullable=True)
    exercise = db.Column(db.String(64), nullable=True)

    # creates a connection from Characteristics -> Breed
    in_breed = db.relationship("Breed", back_populates="char")


class Facts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fact = db.Column(db.String(128), nullable=False)

    # creates a connection from FunnyFacts -> Breed
    breed_fact = db.relationship("Breed", back_populates="fact")


class Breed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    char_id = db.Column(db.Integer, db.ForeignKey("characteristics.id"))
    facts_id = db.Column(db.Integer, db.ForeignKey("facts.id"))

    # creates a connection from Breed -> Group
    in_group = db.relationship("Group", back_populates="breed")
    # creates a connection from Characteristics -> Breed
    char = db.relationship("Characteristics", back_populates="in_breed")
    # creates a connection from FunnyFacts -> Breed
    fact = db.relationship("Facts", back_populates="breed_fact")


db.create_all()
