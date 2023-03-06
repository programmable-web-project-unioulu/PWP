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
    _breed() # init one breed to database
    res = client.post("/api/facts/", json=mockFactBody)
    assert res.status == '201 CREATED'
    assert Facts.query.count() == 1

def test_facts_get(client):
    """
    GET Facts results in empty array if no facts in db, else return all facts in array
    """
    mock_fact = "Test fact for GET method"

    _fact(mock_fact) # init one breed to database
    res = client.get("/api/facts/")
    # decode bytes to string
    data = res.data.decode("utf-8")
    # parse json string
    data = json.loads(data)
    assert data["items"][0]["fact"] == mock_fact

def test_facts_post_unsupported_media(client):
    """
    If request body is not in application/json, raise UnsupportedMedia error 
    """
    # definitely not a JSON
    mock_res_body = 321321312
    res = client.post("/api/group/")
    assert res.status == "415"
