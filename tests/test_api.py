import os
import pytest
import tempfile
import json

from dogdict.models import Group, Characteristics, Facts, Breed
from dogdict import create_app, db


@pytest.fixture
def app():
    db_fd, db_fname = tempfile.mkstemp()
    config = {
        "SQLALCHEMY_DATABASE_URI": "sqlite:///" + db_fname,
        "TESTING": True
    }
    
    app = create_app()
    
    with app.app_context():
        db.create_all()
        
    yield app
    
    with app.app_context():
        db.session.remove()
        db.drop_all()
    os.close(db_fd)
    os.unlink(db_fname)


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
    db.session.add(group)
    db.session.commit()
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
    db.session.add(breed)
    db.session.commit()
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
    db.session.add(fact)
    db.session.commit()
    return fact

# Tests for facts


def test_facts_post(app):
    """
    Can post single facts with proper input
    """
    with app.app_context():
        client = app.test_client()
        _breed()  # init one breed to database
        res = client.post("/api/facts/", json=mockFactBody)
        print(res)
        assert res.status_code == 201
        assert Facts.query.count() == 1


def test_facts_get(app):
    """
    GET Facts results in empty array if no facts in db, else return all facts in array
    """
    mock_fact = "Test fact for GET method"
    with app.app_context():
        client = app.test_client()
        _fact(mock_fact)  # init one breed to database
        res = client.get("/api/facts/")
        # decode bytes to string
        data = res.data.decode("utf-8")
        # parse json string
        data = json.loads(data)
        assert data["items"][0]["fact"] == mock_fact


def test_breeds_post(app):
    """
    GET breeds results in empty array if no facts in db, else return all breeds in array
    """
    with app.app_context():
        client = app.test_client()
        group = _group()
        db.session.add(group)
        db.session.commit()

        res = client.post("/api/breeds/", json=breed1)
        assert res.status_code == 201

        res = client.post("/api/breeds/", json=breed2)
        assert res.status_code == 400

        res = client.post("/api/breeds/", json={"name": "mock", "group": "non-existent"})
        assert res.status_code == 400


def test_breeds_get(app):
    """
    GET breeds returns all breeds from database
    """
    with app.app_context():
        client = app.test_client()
        _breed(True)  # init one breed to database
        res = client.get("/api/breeds/")
        # decode bytes to string
        data = res.data.decode("utf-8")
        # parse json string
        data = json.loads(data)
        assert len(data["items"]) == 1


def test_fact_bad_body(app):
    """
    POST Facts should return BadRequest 400 when bad json body is given in POST request
    method stops in validation
    """
    with app.app_context():
        client = app.test_client()
        bad_body1 = {
            "name2341": "sdfsdf"
        }
        res = client.post('/api/facts/', json=bad_body1)
        assert res.status_code == 400


def test_groups(app):
    """
    First POSTs two groups, then uses GET to make sure there are only two groups
    """
    with app.app_context():
        client = app.test_client()

        res = client.post("/api/groups/", json=group1)
        assert res.status_code == 201

        res = client.post("/api/groups/", json=group2)
        assert res.status_code == 201

        res = client.post("/api/groups/", data=json.dumps(group2))
        assert res.status_code == 415

        res = client.get("/api/groups/")
        data = res.data.decode("utf-8")
        data = json.loads(data)
        assert len(data["items"]) == 2


def test_post_unsupported_media(app):
    """
    If request body is not in correct format, raise UnsupportedMedia error 
    """
    with app.app_context():
        client = app.test_client()
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


def check_duplicates(app):
    """
    Same named groups and breeds can be created only once
    """
    with app.app_context():
        client = app.test_client()
        _group()
        res = client.post("/api/groups/", json=group1)
        assert res.status_code == 201

        res = client.post("/api/groups/", json=group1)
        assert res.status_code == 409

        res = client.post("/api/breeds/", json=breed1)
        assert res.status_code == 201

        res = client.post("/api/breeds/", json=breed1)
        assert res.status_code == 409


def test_delete(app):
    """
        Creates a fact/breed to make sure there is one in the database, then
        deletes it and makes sure it is deleted (status code 204).
        If it doesnt exist returns 404.
    """
    with app.app_context():
        client = app.test_client()
        _breed()  # init one breed to database
        res = client.post("/api/facts/", json=mockFactBody)
        assert res.status_code == 201

        res = client.delete("/api/facts/1/")
        assert res.status_code == 204

def test_characteristics_post(app):
    """
    POST request for characteristics fails if breed is not database
    """
    bad_body ={
        "life_span": 6,
        "in_breed": "non existing breed"
    }
    with app.app_context():
        client = app.test_client()
        res = client.post("/api/characteristics/", json=bad_body)
        assert res.status_code == 404
    
def test_characteristics_post(app):
    """
    Existing breed can be given a characteristic, with different combinations

    """
    with app.app_context():
        client = app.test_client()
        breed = _breed(group=True,name="First good boy")

        good_body = {
            "life_span": 6, # Not nullable
            "in_breed": breed.name
            }

        res = client.post("/api/characteristics/", json=good_body)
        assert res.status_code == 201
        #good_body["exercise"] = 6
        #res2 = client.post("/api/characteristics/", json=good_body)
        #assert res2.status_code == 409

def test_characteristics_post_exercise(app):
    """
        POST request for characteristics is possible with defined exercise value
    """
    with app.app_context():
        client = app.test_client()
        breed = _breed(group=True,name="First good boy")

        good_body = {
            "life_span": 6, # Not nullable
            "in_breed": breed.name,
            "exercise": 4
            }

        res = client.post("/api/characteristics/", json=good_body)
        assert res.status_code == 201

def test_characteristics_post_exercise_and_coatlength(app):
    """
        POST request for characteristics is possible with defined exercise and coat length values
    """
    with app.app_context():
        client = app.test_client()
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


def test_notfound(app):
    """
        Tests if not found error is correctly outputted for breed and group.
        For formatters.
    """
    with app.app_context():
        client = app.test_client()
        res = client.get("/api/breeds/1337/")
        assert res.status_code == 404

        res = client.get("/api/groups/1337/")
        assert res.status_code == 404


def test_put_group(app):
    """
        Group PUT requests return correct responses for valid and invalid bodies
    """
    with app.app_context():
        client = app.test_client()
        res = client.post("/api/groups/", json=group1)
        assert res.status_code == 201

        res = client.put("/api/groups/Test1/", json=group2)
        assert res.status_code == 204

def test_group_validation(app):
    """
    Test that group return bad request 400 with invalid json
    """

    body = {
        "group_name": "value does not exist"
    }
    with app.app_context():
        client = app.test_client()

        res = client.post("/api/groups/", json=body)
        assert res.status_code == 400

def test_group_already_exists(app):
    """
    Returns conflict 409 if named group already exists in db
    """
    group_name = "Fun test group yeah!"

    body = {
        "name": group_name
    }
    with app.app_context():
        client = app.test_client()
        _group(name=group_name)
        res = client.post("/api/groups/", json=body)
        assert res.status_code == 409

def test_breed_already_exists(app):
    """
    Return 409 if named breed already exists in db
    """
    breed_name = "Haha fun breed L0L"

    body = {
        "name": breed_name,
        "group": "Test group"
    }
    with app.app_context():
        client = app.test_client()
        _breed(name=breed_name, group=True)

        res = client.post("/api/breeds/", json=body)
        assert res.status_code == 409

def test_fact_breed_exists(app):
    """
    Return 404 if breed does not exist when giving a fact
    """
    with app.app_context():
        client = app.test_client()
        res = client.post("/api/facts/", json={"fact": "mock fact", "breed": "non existing"})
        assert res.status_code == 404

def test_post_characteristics_duplicate(app):
    """
    Test that POSTs characteristics twice to a breed, resulting in error 409 (1 to 1 relationship)
    """
    body = {
    "in_breed":"test_1",
    "char_id": 1,
    "coat_length": 0.2,
    "life_span": 6,
    "exercise": 1.2
    }
    with app.app_context():
        client = app.test_client()
        _group()
        res = client.post("/api/groups/", json=group1)
        assert res.status_code == 201
        res = client.post("/api/breeds/", json=breed1)
        assert res.status_code == 201
        res = client.post("/api/characteristics/", json=body)
        assert res.status_code == 201
        res = client.post("/api/characteristics/", json=body)
        assert res.status_code == 409

def test_get_characteristics(app):
    """
    All characteristics in db are returned in list
    TODO
    """
    with app.app_context():
        client = app.test_client()
        res = client.get("/api/characteristics/")
        assert res.status_code == 200

def test_group_item_get(app):
    """
    Test that singular group can be found with url, and the uri does not need capitalized group
    """
    with app.app_context():
        client = app.test_client()
        _group(name="Marttionparas")

        res = client.get("/api/groups/marttionparas/")
        data = res.data.decode("utf-8")
        data = json.loads(data)
        assert data == {"name": "Marttionparas"}
    
def test_group_put_validation(app):
    """
    Returns 400 bad request if body does not conform to group schema
    """
    with app.app_context():
        client = app.test_client()
        _group(name="Testgroup123")
        res = client.put("/api/groups/testgroup123/", json={"not_valid": "attribute"})
        assert res.status_code == 400

def test_get_breed(app):
    """
    Test that return breed by id
    """
    with app.app_context():
        client = app.test_client()
        _breed(group=True)

        res = client.get("/api/breeds/1/") # 1 for first id
        data = res.data.decode("utf-8")
        data = json.loads(data)
        assert data == {"name": "Test breed for api", "id": 1, "group": {"name": "Test group", "id": 1}, "facts": []}

def test_put_breed(app):
    """
    Test that breeds name and group can be changed
    """
    # Validation by Breed validator so group is needed, maybe other validator here    
    body = {
        "name": "testbreed200003000",
        "group": "Changegroup"
    }
    with app.app_context():
        client = app.test_client()
        _breed(group=True)
        _group(name="Changegroup") # group to be changed

        res = client.put("/api/breeds/1/", json=body)
        assert res.status_code == 204

def test_put_validation(app):
    """
    PUT method should return 400 for bad body
    """
    body = {
        "martti": "hajottaa"
    }
    with app.app_context():
        client = app.test_client()
        _breed(group=True)
    
        res = client.put("api/breeds/1/", json=body)
        assert res.status_code == 400