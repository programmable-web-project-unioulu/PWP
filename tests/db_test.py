
import pytest
from sqlalchemy.exc import IntegrityError

from tapi.app import app
from tapi.app import db
from tapi.app import Person, Activity

# BEGIN Original fixture setup taken from the Exercise example and then modified further

import os
import tempfile
from sqlalchemy.engine import Engine
from sqlalchemy import event


@pytest.fixture
def dbh():
    db_fd, db_fname = tempfile.mkstemp()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_fname
    app.config["TESTING"] = True

    with app.app_context():
        db.create_all()

    yield db

    db.session.remove()
    os.close(db_fd)
    os.unlink(db_fname)

# TODO: check if this is needed at all
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

# END of the Exercise example origin code

# 'Retrieve an existing instance of the model (recommended trying with different filter options)
# 'Update an existing model instance (if update operation is supported by this model)
# 'Remove an existing model from the database
def test_person_combo(dbh):
    # create original person (id=677) and commit to db
    pid = "677"
    p_original = Person(id=pid)
    dbh.session.add(p_original)
    dbh.session.commit()
    # fetch the original person from the DB as 'fetched'
    fetched = Person.query.filter(Person.id == pid).first()
    assert(fetched.id == pid)
    # change the fetched ID and commit to the DB, primary key still unique
    newid = "677-modified"
    fetched.id = newid
    dbh.session.add(fetched)
    dbh.session.commit()
    # delete the entity
    dbh.session.delete(fetched)
    dbh.session.commit()
    deleted = Person.query.filter(Person.id == newid).first()
    assert(deleted == None)


# TODO: check this part
# 'Test that onModify and onDelete work as expected



def test_person_unique(dbh):
    same_id = "414"
    print("hello")
    p1 = Person(id=same_id)
    p2 = Person(id=same_id)
    dbh.session.add(p1, p2)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()


# 'Create a new instance of the model
def test_person_creation(dbh):
    person = Person()
    person.id = "123"
    dbh.session.add(person)
    dbh.session.commit()

# 'Test possible errors conditions (e.g. foreign keys violation or other situation where Integrity error might be raised)
# Suppress warnings: Person without ID throws IntegrityError,
# but even caught triggers warning in pytest.
@pytest.mark.filterwarnings("ignore")
def test_person_id_required(dbh):
    person = Person()
    dbh.session.add(person)
    try:
        dbh.session.commit()
    except IntegrityError:
        dbh.session.rollback()


# 'Create a new instance of the model
def test_acitivy_creation(dbh):
    activity = Activity()
    activity.id = "123"
    activity.name = "Running"
    activity.intensity = 600 # 600kcal per hour
    dbh.session.add(activity)
    dbh.session.commit()
    # And with optional fields
    a = Activity()
    a.id = "127"
    a.name = "Running-Hard"
    a.intensity = 800  # 600kcal per hour
    a.description = "A harder exercise containing a continuous high heart beat running training"
    dbh.session.add(a)
    dbh.session.commit()
