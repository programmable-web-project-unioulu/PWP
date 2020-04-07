from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.engine import Engine
from sqlalchemy import event

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///job_database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

seek = db.Table("seek",
    db.Column("seeker_id", db.Integer,db.ForeignKey("seeker.id"),primary_key=True),
    db.Column("job_id", db.Integer,db.ForeignKey("job.id"),primary_key=True)
)
provide = db.Table("provide",
    db.Column("job_id", db.Integer, db.ForeignKey("job.id"),primary_key=True),
    db.Column("company_id", db.Integer, db.ForeignKey("company.id"), primary_key=True)
)
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

class jobseeker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=True)
    identify = db.Column(db.String(20), nullable=True)
    specialty = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(20), nullable=True)
    phone_number = db.Column(db.Integer,unique=True)
    desired_position = db.Column(db.String(20), nullable=True)
    desired_address = db.Column(db.String(20), nullable=True)
    CV = db.Column(db.String(400), nullable=True,unique=True)
    jobs = db.relationship("job", secondary=seek, back_populates="jobseekers")
class job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    salary = db.Column(db.String(20), nullable=False)
    introduction = db.Column(db.String(20), nullable=False,unique=True)
    applicant_number = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    region = db.Column(db.String(20), nullable=False)
    jobseekers = db.relationship("jobseeker", secondary=seek, back_populates="jobs")
    companys = db.relationship("company", secondary=provide, back_populates="jobss")
class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(20), nullable=False)
    introduction = db.Column(db.String(20), nullable=False,unique=True)
    phone_number = db.Column(db.Integer, nullable=False,unique=True)
    jobss = db.relationship("job", secondary=provide, back_populates="companys")