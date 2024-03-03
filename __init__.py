from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from extensions import db
from api import api_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db.init_app(app)

app.register_blueprint(api_bp, url_prefix='/api')

# def create_tables():
#     with app.app_context():
#         db.drop_all()
#         db.create_all()
# create_tables()

if __name__ == "__main__":
    app.run(debug=True)
