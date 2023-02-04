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

class Characteristics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    life_span = db.Column(db.String(64), nullable=False)
    coat_length = db.Column(db.String(64), nullable=True)
    exercise = db.Column(db.String(64), nullable=True)

    in_breed = db.relationship("Breed", back_populates="characteristics")

class Facts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fact = db.Column(db.String(128), nullable=False)
    
    # creates a connection from Facts -> Breed
    breed_id = db.Column(db.Integer, db.ForeignKey("breed.id"))
    breed = db.relationship("Breed", back_populates="facts")

class Breed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    char_id = db.Column(db.Integer, db.ForeignKey("characteristics.id"))
    
    # creates a connection from Breed -> Group
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))
    group = db.relationship("Group", back_populates="breeds")
    
    # creates a connection from Breed -> Characteristics
    characteristics = db.relationship("Characteristics", back_populates="in_breed", uselist=False)
    
    # creates a connection from Breed -> Facts
    facts = db.relationship("Facts", back_populates="breed")



db.create_all()
