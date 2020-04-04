##Based on the resource_test.py on lovelace "Testing Flask Applications part 2

import json
import os
import pytest
import tempfile
import time

from datetime import datetime
from jsonschema import validate
from sqlalchemy.engine import Engine
from sqlalchemy import event
from sqlalchemy.exc import IntegrityError, StatementError

from app import app
#app = Flask(__name__), db = SQLAlchemy(app)

from db.db import db, Articles, Users, AddedArticles

##imports that are in app.py
from flask import Flask, redirect
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from src.resources.entrypoint import EntryPoint
from src.resources.articleresource import ArticleCollection, ArticleItem
from src.resources.userresource import UserCollection, UserItem
from src.resources.addedarticleresource import AddedArticleCollection, AddedArticleItem

##listener for? (from example)
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

## Test for the database
@pytest.fixture
def client():
    db_fd, db_fname = tempfile.mkstemp()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_fname
    app.config["TESTING"] = True

    db.create_all()
    populate_db()
    #note that the db exists already...

    yield app.test_client()

    db.session.remove()
    os.close(db_fd)
    os.unlink(db_fname)

##DATABASE POPULATING
#populate database with (now with one of each only) 
def populate_db():
    _article_populate()
    _user_populate()
    _added_article_populate()

def _article_populate():
    article = Articles(
        date='02.01.2026',
        link='https://justtesting.com', 
        headline="API coder is angry", 
        modtime=datetime.now()
    )
    db.session.add(article)
    db.session.commit()

def _user_populate():
    user = Users(username='sample500')
    db.session.add(user)
    db.session.commit()
    
def _added_article_populate():
    user = Users(username='sample505')

    addedarticle = AddedArticles(
        headline="Test added article", 
        modtime=datetime.now(), 
        owner=user
    )
    db.session.add(addedarticle)
    db.session.commit()

### TESTS
#build tests for classes

def _check_control_post(self, client):
    #Validate controls
    ctrl_obj = obj["@controls"][ctrl]
    href = ctrl_obj["href"]
    method = ctrl_obj["method"].lower()
    encoding = ctrl_obj["encoding"].lower()
    schema = ctrl_obj["schema"]
    
    assert method == "post"
    assert encoding == "json"
    
    #check with json formatted user data, not used before, could use function/argument...
    body = {"username": 'sample501'}
    validate(body, schema)
    resp = client.post(href, json=body)
    assert resp.status_code == 201


class TestUserCollection(object):
    '''
    Checks that the user collection work properly
    '''
    RESOURCE_URL = "/api/users/"

    def test_post(self, client):

        ##todo: function
        valid = {"username": 'sample503'}

        ##check with wrong content type
        resp = client.post(self.RESOURCE_URL, data=json.dumps(valid))
        assert resp.status_code == 415
