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

#import app and db-builder
from app import app
from db.db import db, Articles, Users, AddedArticles

##imports that are in app.py
from flask import Flask, redirect
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from src.resources.entrypoint import EntryPoint
from src.resources.articleresource import ArticleCollection, ArticleItem
from src.resources.userresource import UserCollection, UserItem
from src.resources.addedarticleresource import AddedArticleCollection, AddedArticleItem

## forgot what this was for?
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

## Pytest setup
@pytest.fixture
def client():   
    #clean database before running
    #(had issues with previous data)
    ##CLEANS ALL DB!
    db.drop_all()
    
    db_fd, db_fname = tempfile.mkstemp()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_fname
    app.config["TESTING"] = True

    db.create_all()
    
    populate_db()

    yield app.test_client()

    db.session.remove()

    #clean db after also, unless debugging problems in this file
    #db.drop_all()
    
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
        date='01.01.2020',
        link='https://justtesting.com', 
        headline="Tests are running", 
        modtime=datetime.now()
    )
    db.session.add(article)
    db.session.commit()

def _user_populate():
    user = Users(username='user1')
    db.session.add(user)
    db.session.commit()
    
def _added_article_populate():

    addedarticle = AddedArticles(
        link='https://added.test',
        headline="This is an added article", 
        modtime=datetime.now(),
        owner_username="user1"
        ##use either of these:
        #owner=Users(username="") creates new user
        #owner_username="" uses existing user
        #file conffed for 1 user
    )
    db.session.add(addedarticle)
    db.session.commit()

### TESTS
#pytest runs all function starting with "test"

#check that the populated database exists now
def test_check_db():
    ##I don't understand what is the order of the tests
    #if there is other test that adds and doesn't remove, this may fail

    #check article
    assert Articles.query.count() == 1
    testArticle = Articles.query.first()
    assert testArticle.date == '01.01.2020'

    #check user
    assert Users.query.count() == 1
    testUser = Users.query.first()
    assert testUser.username == 'user1'

    #check added article
    assert AddedArticles.query.count() == 1
    testAdded = AddedArticles.query.first()
    assert testAdded.headline == 'This is an added article'

    

'''
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
    body = {"username": 'test1'}
    validate(body, schema)
    resp = client.post(href, json=body)
    assert resp.status_code == 201
'''


class TestUserCollection(object):
    '''
    Checks that the user collection work properly
    '''
    RESOURCE_URL = "/api/users/"

    def test_post(self, client):
        #checks responses:
        #201, 400, 409, 415
        #also deletes at the end

        testUser = {"username": 'test2'}

        ##check with wrong content type
        resp = client.post(self.RESOURCE_URL, data=json.dumps(testUser))
        assert resp.status_code == 415

        #check without username (without data gives 415)
        resp = client.post(self.RESOURCE_URL, json={"asd": "false"})
        assert resp.status_code == 400

        #test with valid, verify
        resp = client.post(self.RESOURCE_URL, json=testUser)
        assert resp.status_code == 201

        #should be found from 
        #'/api/users/{}/'.format(username)
        #http://127.0.0.1:5000/api/users/test2/
        assert resp.headers["Location"].endswith(self.RESOURCE_URL + "test2" + "/")

        #check posting with the same name
        resp = client.post(self.RESOURCE_URL, json=testUser)
        assert resp.status_code == 409

        #delete the user (otherwise messes up database query counts)
        resp = client.delete(self.RESOURCE_URL + "test2" + "/")
        
        
