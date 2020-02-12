import os
import pytest
import tempfile
from datetime import datetime
from sqlalchemy.exc import IntegrityError

import db as app
from db import January, February, March, April, May, June, July, August, September, October, November, December

@pytest.fixture
def db_handle():
    db_fd, db_fname = tempfile.mkstemp()
    app.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_fname
    app.app.config["TESTING"] = True
    
    with app.app.app_context():
        app.db.create_all()
        
    yield app.db
    
    app.db.session.remove()
    os.close(db_fd)
    os.unlink(db_fname)

# January table test
def test_january(db_handle):

    # Test entry creation
    entry = January(link='https://www.google.com/', headline="First headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert January.query.count() == 1

    # Test getting an entry
    entry = January.query.filter_by(date=1).first()
    assert entry.headline == "First headline"

    # Test deletion of an entry
    entry = January(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert January.query.count() == 2
    entry = January.query.filter_by(date=2).first()
    db_handle.session.delete(entry)
    db_handle.session.commit()
    entry = January.query.first()
    assert entry.headline == "First headline"

    # Test modification of an entry
    entry = January.query.first()
    entry.headline = "New headline"
    db_handle.session.commit()
    entry = January.query.first()
    entry.headline = "New headline"

    # Test that date is unique
    entry = January(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert January.query.filter_by(date=2).first().date == 2
    entry = January.query.filter_by(date=2).first()
    entry.date = 1
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that headline can't be null
    entry = January.query.first()
    entry.headline = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that modtime can't be null
    entry = January.query.first()
    entry.modtime = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()