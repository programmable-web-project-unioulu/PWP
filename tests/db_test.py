
import pytest
from sqlalchemy.exc import IntegrityError

from tapi.app import app
from tapi.app import db
from tapi.app import Person

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


def test_person_creation(dbh):
    person = Person()
    person.id = "123"
    dbh.session.add(person)
    dbh.session.commit()

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
