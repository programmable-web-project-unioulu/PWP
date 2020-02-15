from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class January(db.Model):
    date = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(256), nullable=True)
    headline = db.Column(db.String(128), nullable=False)
    modtime = db.Column(db.DateTime, nullable=False)
	
class February(db.Model):
    date = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(256), nullable=True)
    headline = db.Column(db.String(128), nullable=False)
    modtime = db.Column(db.DateTime, nullable=False)

class March(db.Model):
    date = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(256), nullable=True)
    headline = db.Column(db.String(128), nullable=False)
    modtime = db.Column(db.DateTime, nullable=False)

class April(db.Model):
    date = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(256), nullable=True)
    headline = db.Column(db.String(128), nullable=False)
    modtime = db.Column(db.DateTime, nullable=False)

class May(db.Model):
    date = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(256), nullable=True)
    headline = db.Column(db.String(128), nullable=False)
    modtime = db.Column(db.DateTime, nullable=False)

class June(db.Model):
    date = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(256), nullable=True)
    headline = db.Column(db.String(128), nullable=False)
    modtime = db.Column(db.DateTime, nullable=False)

class July(db.Model):
    date = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(256), nullable=True)
    headline = db.Column(db.String(128), nullable=False)
    modtime = db.Column(db.DateTime, nullable=False)

class August(db.Model):
    date = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(256), nullable=True)
    headline = db.Column(db.String(128), nullable=False)
    modtime = db.Column(db.DateTime, nullable=False)

class September(db.Model):
    date = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(256), nullable=True)
    headline = db.Column(db.String(128), nullable=False)
    modtime = db.Column(db.DateTime, nullable=False)

class October(db.Model):
    date = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(256), nullable=True)
    headline = db.Column(db.String(128), nullable=False)
    modtime = db.Column(db.DateTime, nullable=False)

class November(db.Model):
    date = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(256), nullable=True)
    headline = db.Column(db.String(128), nullable=False)
    modtime = db.Column(db.DateTime, nullable=False)

class December(db.Model):
    date = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(256), nullable=True)
    headline = db.Column(db.String(128), nullable=False)
    modtime = db.Column(db.DateTime, nullable=False)

class AddedArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(256), nullable=True)
    headline = db.Column(db.String(128), nullable=False)
    modtime = db.Column(db.DateTime, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    owner = db.relationship("Users", back_populates="article")

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(32), nullable=False)
    article = db.relationship("AddedArticle", back_populates="owner")
