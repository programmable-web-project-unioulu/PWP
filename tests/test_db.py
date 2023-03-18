import os
import pytest
import tempfile
from dogdict import create_app, db
from dogdict.models import Group, Characteristics, Facts, Breed
from sqlalchemy.engine import Engine
from sqlalchemy import event
from sqlalchemy.exc import IntegrityError


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""
Fixture to create the app and clear db for every test, this fixture is partially copied from course lovelace
"""
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

# Fixture to setup and teardown a db for each test
"""
@pytest.fixture
def app():
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
    """

# Configuration for db
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

def _breed(app=None, group=False, fact=False, chars=False):
    if group and chars:
        group = Group(
            name="Test group"
        )

        characteristics = _characteristics()

        db.session.add(group)
        db.session.add(characteristics)
        db.session.commit()

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

        db.session.add(group)
        db.session.commit()

        return Breed(
            name="Test breed",
            group=group,
            facts = [fact]
        )
    
    if group:
        group = Group(
            name="Test group"
        )

        db.session.add(group)
        db.session.commit()

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

def test_create_breed(app):
    """
    Test that a Breed can be created with proper input
    """
    with app.app_context():
        new_breed = _breed()
        db.session.add(new_breed)
        db.session.commit()

        assert Breed.query.count() == 1

def test_fail_breed(app):
    """
    Test that breed cannot be commited without proper input
    """
    with app.app_context():
        db.session.add(Breed())
        with pytest.raises(IntegrityError):
            db.session.commit()

def test_unique_breed_name(app):
    """
    Test that duplicate breeds can not be added to db
    """
    with app.app_context():
        breed1 = _breed()
        breed2 = _breed()
        db.session.add(breed1)
        db.session.add(breed2)

        with pytest.raises(IntegrityError):
            db.session.commit()

def test_breed_serializer_short(app):
    """
    Test that short form breed serializer returns object with name
    """
    with app.app_context():
        breed = _breed()
        db.session.add(breed)
        db.session.commit()

        assert breed.serialize(True) == { 'name': 'Test breed', "id": 1}


def test_breed_serializer_long(app):
    """
    Test breed serializer returns proper object when facts are included
    """
    with app.app_context():
        breed = _breed(app, group=True, fact=True)

        assert breed.serialize() == {
            "group" : {"id": 1, "name" : "Test group"},
            "name": "Test breed",
            "facts": ["Test fact for breed"],
            "id": None
        }

def test_breed_serializer_long_w_characteristics(app):
    """
    Test breed serializer when breed has characteristics information included
    """
    with app.app_context():
        breed = _breed(app, group=True, fact=False, chars=True)

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

def test_breed_deserializer(app):
    """
    Breed deserialize works properly
    """
    with app.app_context():
        breed = _breed(app, group=True)
        breed.deserialize(doc={"name": "Breed name", "group": "test change group"})
    
        assert breed.name == "Breed name"

def test_breed_json_schema():
    """
    Breed json schema should require name and group
    """
    breed = _breed()
    assert breed.json_schema()["required"] == ["name", "group"]

## FACTS test

def test_add_fact_without_breed(app):
    """
    Test that fact can be added without prior breed information
    """
    with app.app_context():
        fact = _fact()
        db.session.add(fact)
        assert Facts.query.count() == 1

def test_fail_fact(app):
    """
    Test that fact cannot be added to db without proper input
    """
    with app.app_context():
        db.session.add(Facts())
        with pytest.raises(IntegrityError):
            db.session.commit()

def test_fact_serializer(app):
    """
    Fact serialize returns fact, serialized breed --> serialized group
    """
    with app.app_context():
        breed = _breed(app, group=True)

        fact = Facts(
            fact="Test fact for breed",
            breed=breed
        )
        db.session.add(fact)
        db.session.add(breed)
        db.session.commit()

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

def test_add_group(app):
    """
    Group with unique name can be added to db
    """
    with app.app_context():
        group = _group()

        db.session.add(group)
        db.session.commit()

        assert Group.query.count() == 1

def test_fail_group(app):
    """
    Group without name / proper input causes integrity error
    """
    with app.app_context():
        db.session.add(Group())
        with pytest.raises(IntegrityError):
            db.session.commit()

def test_group_serializer(app):
    """
    Test group serialize returns first id and the name
    """
    with app.app_context():
        group = _group()
        db.session.add(group)
        db.session.commit()

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

def test_characteristics_serializer(app):
    """
    Characteristics serializer returns breed, char_id, coat_length, exercise ...
    """
    with app.app_context():
        char = _characteristics()
        db.session.add(char)
        db.session.commit()

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
