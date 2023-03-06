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
    "group": "Test group"
}

breed2 = {
    "asd": "test_2",
}

breed3 = {
    "name": "test_3",
    "group": "Terrier3"
}


def _group(name="Test group"):
    """
    Init one group to database and return it
    """
    group = Group(
        name=name
    )
    app.db.session.add(group)
    app.db.session.commit()
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

    res = client.post("/api/breeds/", json={"name": "mock", "group": "non-existent"})
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

    _group(name="Testgroup123")
    res = client.put("/api/groups/testgroup123/", data=mock_body)
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
    res = client.delete("/api/breeds/1/")
    assert res.status_code == 204

    res = client.delete("/api/facts/1337/")
    assert res.status_code == 404

    res = client.delete("/api/breeds/1337/")
    assert res.status_code == 404


def test_notfound(client):
    """
        Tests if not found error is correctly outputted for breed and group.
        For formatters.
    """
    res = client.get("/api/breeds/1337/")
    assert res.status_code == 404

    res = client.get("/api/groups/1337/")
    assert res.status_code == 404


def test_put_group(client):
    """
        Tests if put is possible.
    """

    res = client.post("/api/groups/", json=group1)
    assert res.status_code == 201

    res = client.put("/api/groups/Test1/", json=group2)
    assert res.status_code == 204

def test_group_validation(client):
    """
    Test that group return bad request 400 with invalid json
    """

    body = {
        "group_name": "value does not exist"
    }

    res = client.post("/api/groups/", json=body)
    assert res.status_code == 400

def test_group_already_exists(client):
    """
    Returns conflict 409 if named group already exists in db
    """
    group_name = "Fun test group yeah!"
    _group(name=group_name)

    body = {
        "name": group_name
    }

    res = client.post("/api/groups/", json=body)
    assert res.status_code == 409

def test_breed_already_exists(client):
    """
    Return 409 if named breed already exists in db
    """
    breed_name = "Haha fun breed L0L"
    _breed(name=breed_name, group=True)

    body = {
        "name": breed_name,
        "group": "Test group"
    }

    res = client.post("/api/breeds/", json=body)
    assert res.status_code == 409

def test_fact_breed_exists(client):
    """
    Return 404 if breed does not exist when giving a fact
    """
    res = client.post("/api/facts/", json={"fact": "mock fact", "breed": "non existing"})
    assert res.status_code == 404

def test_get_characteristics(client):
    """
    All characteristics in db are returned in list
    TODO
    """

    res = client.get("/api/characteristics/")
    assert res.status_code == 200

def test_group_item_get(client):
    """
    Test that singular group can be found with url, and the uri does not need capitalized group
    """
    _group(name="Marttionparas")

    res = client.get("/api/groups/marttionparas/")
    data = res.data.decode("utf-8")
    data = json.loads(data)
    assert data == {"name": "Marttionparas"}
    
def test_group_put_validation(client):
    """
    Returns 400 bad request if body does not conform to group schema
    """
    _group(name="Testgroup123")
    res = client.put("/api/groups/testgroup123/", json={"not_valid": "attribute"})
    assert res.status_code == 400

def test_get_breed(client):
    """
    Test that return breed by id
    """
    _breed(group=True)

    res = client.get("/api/breeds/1/") # 1 for first id
    data = res.data.decode("utf-8")
    data = json.loads(data)
    assert data == {"name": "Test breed for api", "id": 1, "group": {"name": "Test group", "id": 1}, "facts": []}

def test_put_breed(client):
    """
    Test that breeds name and group can be changed
    """
    _breed(group=True)
    _group(name="Changegroup") # group to be changed

    # Validation by Breed validator so group is needed, maybe other validator here    
    body = {
        "name": "testbreed200003000",
        "group": "Changegroup"
    }

    res = client.put("/api/breeds/1/", json=body)
    assert res.status_code == 204

def test_put_validation(client):
    """
    PUT method should return 400 for bad body
    """
    _breed(group=True)
    body = {
        "martti": "hajottaa"
    }

    res = client.put("api/breeds/1/", json=body)
    assert res.status_code == 400