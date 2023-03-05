import os
import pytest
import tempfile
import database as app

from database import Group, Characteristics, Facts, Breed
from sqlalchemy.engine import Engine
from sqlalchemy import event
from sqlalchemy.exc import IntegrityError
import api


# Fixture to setup and teardown a db for each test
@pytest.fixture
def db_handle():
    db_fd, db_fname = tempfile.mkstemp()
    app.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_fname
    app.app.config["TESTING"] = True
    
    with app.app.app_context():
        app.db.create_all()
        
    yield app.db
    
    app.db.session.remove()
    app.db.drop_all()
    os.close(db_fd)
    os.unlink(db_fname)

# Configuration for db
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

def _breed(db_handle=None, group=False, fact=False, chars=False):
    if group and chars:
        group = Group(
            name="Test group"
        )

        characteristics = _characteristics()

        db_handle.session.add(group)
        db_handle.session.add(characteristics)
        db_handle.session.commit()

        return Breed(
            name="Test breed",
            group=group,
            characteristics=characteristics
        )
    
    if group and fact:
        group = Group(
            name="Test group"
        )

        fact = _fact()

        db_handle.session.add(group)
        db_handle.session.commit()

        return Breed(
            name="Test breed",
            group=group,
            facts = [fact]
        )
    
    if group:
        group = Group(
            name="Test group"
        )

        db_handle.session.add(group)
        db_handle.session.commit()

        return Breed(
            name="Test breed",
            group=group,
        )
    
    return Breed(
        name="Test breed"
    )

def _characteristics():
    return Characteristics(
        life_span=6
    )

def _fact():
    return Facts(
        fact="Test fact for breed"
    )

def _group():
    return Group(
        name="Test group"
    )
    

##############
# BREED TEST #
##############

def test_create_breed(db_handle):
    """
    Test that a Breed can be created with proper input
    """
    new_breed = _breed()
    db_handle.session.add(new_breed)
    db_handle.session.commit()

    assert Breed.query.count() == 1

def test_fail_breed(db_handle):
    """
    Test that breed cannot be commited without proper input
    """
    db_handle.session.add(Breed())
    with pytest.raises(IntegrityError):
        db_handle.session.commit()

def test_unique_breed_name(db_handle):
    """
    Test that duplicate breeds can not be added to db
    """
    breed1 = _breed()
    breed2 = _breed()
    db_handle.session.add(breed1)
    db_handle.session.add(breed2)

    with pytest.raises(IntegrityError):
        db_handle.session.commit()

def test_breed_serializer_short(db_handle):
    """
    Test that short form breed serializer returns object with name
    """
    breed = _breed()
    db_handle.session.add(breed)
    db_handle.session.commit()

    assert breed.serialize(True) == { 'name': 'Test breed', "id": 1}


def test_breed_serializer_long(db_handle):
    """
    Test breed serializer returns proper object when facts are included
    """
    breed = _breed(db_handle, group=True, fact=True)

    assert breed.serialize() == {
        "group" : {"id": 1, "name" : "Test group"},
        "name": "Test breed",
        "facts": ["Test fact for breed"],
        "id": None
    }

def test_breed_serializer_long_w_characteristics(db_handle):
    """
    Test breed serializer when breed has characteristics information included
    """
    breed = _breed(db_handle, group=True, fact=False, chars=True)

    assert breed.serialize() == {
        "group" : {"id": 1, "name" : "Test group"},
        "name": "Test breed",
        "facts": [],
        "characteristics": {
            "char_id": 1,
            "exercise": None,
            "coat_length": None,
            "life_span": 6
        },
        "id": None
    }

def test_breed_deserializer():
    """
    Breed deserialize works properly
    """
    breed = _breed()
    breed.deserialize(doc={"name": "Breed name"})
    
    assert breed.name == "Breed name"

def test_breed_json_schema():
    """
    Breed json schema should require name and group
    """
    breed = _breed()

    assert breed.json_schema()["required"] == ["name", "group"]

## FACTS test

def test_add_fact_without_breed(db_handle):
    """
    Test that fact can be added without prior breed information
    """
    fact = _fact()

    db_handle.session.add(fact)

    assert Facts.query.count() == 1

def test_fail_fact(db_handle):
    """
    Test that fact cannot be added to db without proper input
    """
    db_handle.session.add(Facts())
    with pytest.raises(IntegrityError):
       db_handle.session.commit()

def test_fact_serializer(db_handle):
    """
    Fact serialize returns fact, serialized breed --> serialized group
    """
    breed = _breed(db_handle, group=True)

    fact = Facts(
        fact="Test fact for breed",
        breed=breed
    )
    db_handle.session.add(fact)
    db_handle.session.add(breed)
    db_handle.session.commit()

    assert fact.serialize() == {
        "fact": "Test fact for breed",
        "breed": {
            "facts": ["Test fact for breed"],
            "group": {"id": 1, "name": "Test group"},
            "name": "Test breed",
            "id": 1
        },
        "id": 1
    }

def test_facts_json_schema():
    """
    Fact json schema requires fact and breed
    """
    fact = _fact()
    
    assert fact.json_schema()["required"] == ["fact", "breed"]

# GROUP TESTS

def test_add_group(db_handle):
    """
    Group with unique name can be added to db
    """
    group = _group()

    db_handle.session.add(group)
    db_handle.session.commit()

    assert Group.query.count() == 1

def test_fail_group(db_handle):
    """
    Group without name / proper input causes integrity error
    """

    db_handle.session.add(Group())
    with pytest.raises(IntegrityError):
        db_handle.session.commit()

def test_group_serializer(db_handle):
    """
    Test group serialize returns first id and the name
    """
    group = _group()
    db_handle.session.add(group)
    db_handle.session.commit()

    assert group.serialize() == {"id": 1, "name": "Test group"}

def test_group_deserializer():
    """
    Group serializer returns correct output
    """
    group = _group()
    group.deserialize(doc={"name": "New group name"})

    assert group.name == "New group name"

def test_group_json_schema():
    """
    Test that group schema requires name
    """

    group = _group()

    assert group.json_schema()["required"] == ['name']

# CHARACTERISTICS tests

def test_characteristics_serializer(db_handle):
    """
    Characteristics serializer returns breed, char_id, coat_length, exercise ...
    """
    char = _characteristics()
    db_handle.session.add(char)
    db_handle.session.commit()

    assert char.serialize() == {
        "breed": [],
        "char_id": 1,
        "coat_length": None,
        "life_span": 6,
        "exercise": None
    }

def test_characteristics_json_schema():
    """
    Characteristics schema should require in what breed and life span inputs
    """
    char = _characteristics()
    
    assert char.json_schema()["required"] == ["in_breed", "life_span"]
