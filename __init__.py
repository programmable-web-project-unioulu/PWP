from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from extensions import db
from api import api_bp

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config["SQLALCHEMY_DATABASE_BASE_URI"] = "mysql+mysqldb://root@localhost/"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqldb://admin:pwpdb7788@workoutplaylists.cpcoaea0i7dq.us-east-1.rds.amazonaws.com/workout_playlists"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
