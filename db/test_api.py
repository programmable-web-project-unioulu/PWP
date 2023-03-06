import os
import pytest
import tempfile
import json

from database import Group, Characteristics, Facts, Breed
from sqlalchemy.engine import Engine
from sqlalchemy import event
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound, Conflict, BadRequest, UnsupportedMediaType
import database as app


@pytest.fixture
def client():
    db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
    app.app.config['TESTING'] = True

    with app.app.test_client() as client:
        with app.app.app_context():
            app.db.create_all()
        yield client

    app.db.session.remove()
    app.db.drop_all()
    os.close(db_fd)
    os.unlink(app.app.config['DATABASE'])


mockFactBody = {
    "breed": "Test breed for api",
    "fact": "Test fact for breed"
}


def _group():
    """
    Init one group to database and return it
    """
    group = Group(
        name="New fun group"
    )
    return group


def _breed(group=False, name="Test breed for api"):
    """
    Init one breed to database and return the breed
    """
    if group:
        breed = Breed(
            name=name,
            group=_group(),
        )
    else:
        breed = Breed(
            name=name
        )
    app.db.session.add(breed)
    app.db.session.commit()
    return breed


def _fact(fact="Fun test fact"):
    """
    Init one fact to database
    """
    breed = _breed(group=True)
    fact = Facts(
        fact=fact,
        breed=breed
    )
    app.db.session.add(fact)
    app.db.session.commit()
    return fact

# Tests for facts


def test_facts_post(client):
    """
    Can post single facts with proper input
    """
    _breed()  # init one breed to database
    res = client.post("/api/facts/", json=mockFactBody)
    assert res.status == '201 CREATED'
    assert Facts.query.count() == 1


def test_facts_get(client):
    """
    GET Facts results in empty array if no facts in db, else return all facts in array
    """
    mock_fact = "Test fact for GET method"

    _fact(mock_fact)  # init one breed to database
    res = client.get("/api/facts/")
    # decode bytes to string
    data = res.data.decode("utf-8")
    # parse json string
    data = json.loads(data)
    assert data["items"][0]["fact"] == mock_fact


def test_breeds_get(client):
    """
    GET breeds results in empty array if no facts in db, else return all breeds in array
    """

    _breed(True)  # init one breed to database
    res = client.get("/api/breeds/")
    # decode bytes to string
    data = res.data.decode("utf-8")
    # parse json string
    data = json.loads(data)
    print(data["items"])
    assert len(data["items"]) == 1


def test_groups_get(client):
    """
    GET groups results in empty array if no facts in db, else return all groups in array
    """
    _group()
    _breed(True)
    group1 = {
        "name": "test_name"
    }
    res=client.post("/api/groups/", json=group1)
    assert res.status_code == 201
    res = client.get("/api/groups/")
    data = res.data.decode("utf-8")
    data = json.loads(data)
    print(data)
    assert len(data["items"]) == 2


def test_post_unsupported_media(client):
    """
    If request body is not in correct format, raise UnsupportedMedia error 
    """
    _breed()
    mock_body = {'asd': 'asd', 'perkele': 'perkele'}
    res = client.post("/api/facts/", data=mock_body)
    assert res.status_code == 415
    res = client.post("/api/groups/", data=mock_body)
    assert res.status_code == 415
    res = client.post("/api/breeds/", data=mock_body)
    assert res.status_code == 415


def test_facts_delete(client):
    """
        Creates a fact to make sure there is one in the database, then
        deletes it and makes sure it is deleted (status code 204).
    """
    _breed()  # init one breed to database
    res = client.post("/api/facts/", json=mockFactBody)
    assert res.status_code == 201
    res = client.delete("/api/facts/1/")
    assert res.status_code == 204

def test_characteristics_post(client):
    """
    
    """
    bad_body ={
        "life_span": 6,
        "in_breed": "non existing breed"
    }

    res = client.post("/api/characteristics/", json=bad_body)
    assert res.status_code == 404
    
def test_characteristics_post(client):
    """
    Existing breed can be given a characteristic, with different combinations

    """
    breed = _breed(group=True,name="First good boy")

    good_body = {
        "life_span": 6, # Not nullable
        "in_breed": breed.name
        }

    res = client.post("/api/characteristics/", json=good_body)
    assert res.status_code == 201
    good_body["exercise"] = 6
    res2 = client.post("/api/characteristics/", json=good_body)
    assert res2.status_code == 409

def test_characteristics_post_exercise(client):
    """
    
    """
    breed = _breed(group=True,name="First good boy")

    good_body = {
        "life_span": 6, # Not nullable
        "in_breed": breed.name,
        "exercise": 4
        }

    res = client.post("/api/characteristics/", json=good_body)
    assert res.status_code == 201

def test_characteristics_post_exercise_and_coatlength(client):
    """
    
    """
    breed = _breed(group=True,name="First good boy")

    good_body = {
        "life_span": 6, # Not nullable
        "in_breed": breed.name,
        "exercise": 4,
        "coat_length": 2
        }

    res = client.post("/api/characteristics/", json=good_body)
    assert res.status_code == 201
