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

group1 = {
    "name": "Test1"
}

group2 = {
    "name": "Test2"
}


breed1 = {
    "name": "test_1",
    "group": "New fun group"
}

breed2 = {
    "asd": "test_2",
}

breed3 = {
    "name": "test_3",
    "group": "Terrier3"
}


def _group():
    """
    Init one group to database and return it
    """
    group = Group(
        name="New fun group"
    )
    return group


def _breed(group=False):
    """
    Init one breed to database and return the breed
    """
    if group:
        breed = Breed(
            name="Test breed for api",
            group=_group(),
        )
    else:
        breed = Breed(
            name="Test breed for api"
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
    assert res.status_code == 201
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


def test_breeds_post(client):
    """
    GET breeds results in empty array if no facts in db, else return all breeds in array
    """

    group = _group()
    app.db.session.add(group)
    app.db.session.commit()

    res = client.post("/api/breeds/", json=breed1)
    assert res.status_code == 201

    res = client.post("/api/breeds/", json=breed2)
    assert res.status_code == 400

    # res = client.post("/api/breeds/", json=breed3)
    # assert res.status_code == 400


def test_breeds_get(client):
    _breed(True)  # init one breed to database
    res = client.get("/api/breeds/")
    # decode bytes to string
    data = res.data.decode("utf-8")
    # parse json string
    data = json.loads(data)
    print(data["items"])
    assert len(data["items"]) == 1


def test_fact_bad_body(client):
    """
    POST Facts should return BadRequest 400 when bad json body is given in POST request
    method stops in validation
    """
    bad_body1 = {
        "name2341": "sdfsdf"
    }
    res = client.post('/api/facts/', json=bad_body1)
    assert res.status_code == 400


def test_groups(client):
    """
    First POSTs two groups, then uses GET to make sure there are only two groups
    """

    res = client.post("/api/groups/", json=group1)
    assert res.status_code == 201

    res = client.post("/api/groups/", json=group2)
    assert res.status_code == 201

    res = client.post("/api/groups/", data=json.dumps(group2))
    assert res.status_code == 415

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

    res = client.post("/api/characteristics/", data=mock_body)
    assert res.status_code == 415


def check_duplicates(client):
    _group()
    print("HELLO??")
    res = client.post("/api/groups/", json=group1)
    assert res.status_code == 201

    res = client.post("/api/groups/", json=group1)
    assert res.status_code == 409

    res = client.post("/api/breeds/", json=breed1)
    assert res.status_code == 201

    res = client.post("/api/breeds/", json=breed1)
    assert res.status_code == 409


def test_delete(client):
    """
        Creates a fact/breed to make sure there is one in the database, then
        deletes it and makes sure it is deleted (status code 204).
        If it doesnt exist returns 404.
    """
    _breed()  # init one breed to database
    res = client.post("/api/facts/", json=mockFactBody)
    assert res.status_code == 201

    res = client.delete("/api/facts/1/")
    assert res.status_code == 204

    res = client.delete("/api/breeds/1/")
    assert res.status_code == 204

    res = client.delete("/api/facts/1337/")
    assert res.status_code == 404

    res = client.delete("/api/breeds/1337/")
    assert res.status_code == 404


def test_notfound(client):
    """
        Tests if not found error is correctly outputted.
        For formatters.
    """
    res = client.get("/api/breeds/1337/")
    assert res.status_code == 404

    res = client.get("/api/groups/1337/")
    assert res.status_code == 404


def test_put(client):
    """
        Tests if put is possible.
    """

    res = client.post("/api/groups/", json=group1)
    assert res.status_code == 201

    res = client.put("/api/groups/Test1/", json=group2)
    assert res.status_code == 204
