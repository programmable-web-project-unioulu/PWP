import os
import json
from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
from .constants import *


db = SQLAlchemy()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI="sqlite:///" + os.path.join("development.db"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    from . import models
    from . import api

    app.cli.add_command(models.init_db_command)
    app.register_blueprint(api.api_bp)

    @app.route("/profiles/<profile>/")
    def send_profile(profile):
        return "you requests {} profile".format(profile)

    @app.route(LINK_RELATIONS_URL)
    def send_link_relations():
        return "link relations"

    @app.route("/api/")
    def index():
        body = {
            "@namespaces":{
                "plandi": {
                    "name":"/plandi/link-relations/#"
                }
            },
            "controls":{
                "plandi:plants-all": {
                    "href":"/api/plants/"
                },
                "plandi:species-all": {
                    "href":"/api/species/"
                },
                "plandi:plantdiary":{
                    "href":"/api/plantdiary"
                }
            }
        }
        return Response(
            status=200,
            response=json.dumps(body),
            mimetype=MASON
        )

    return app
