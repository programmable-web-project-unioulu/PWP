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
def test_January(db_handle):

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

# February table test
def test_February(db_handle):

    # Test entry creation
    entry = February(link='https://www.google.com/', headline="First headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert February.query.count() == 1

    # Test getting an entry
    entry = February.query.filter_by(date=1).first()
    assert entry.headline == "First headline"

    # Test deletion of an entry
    entry = February(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert February.query.count() == 2
    entry = February.query.filter_by(date=2).first()
    db_handle.session.delete(entry)
    db_handle.session.commit()
    entry = February.query.first()
    assert entry.headline == "First headline"

    # Test modification of an entry
    entry = February.query.first()
    entry.headline = "New headline"
    db_handle.session.commit()
    entry = February.query.first()
    entry.headline = "New headline"

    # Test that date is unique
    entry = February(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert February.query.filter_by(date=2).first().date == 2
    entry = February.query.filter_by(date=2).first()
    entry.date = 1
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that headline can't be null
    entry = February.query.first()
    entry.headline = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that modtime can't be null
    entry = February.query.first()
    entry.modtime = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()

# March table test
def test_March(db_handle):

    # Test entry creation
    entry = March(link='https://www.google.com/', headline="First headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert March.query.count() == 1

    # Test getting an entry
    entry = March.query.filter_by(date=1).first()
    assert entry.headline == "First headline"

    # Test deletion of an entry
    entry = March(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert March.query.count() == 2
    entry = March.query.filter_by(date=2).first()
    db_handle.session.delete(entry)
    db_handle.session.commit()
    entry = March.query.first()
    assert entry.headline == "First headline"

    # Test modification of an entry
    entry = March.query.first()
    entry.headline = "New headline"
    db_handle.session.commit()
    entry = March.query.first()
    entry.headline = "New headline"

    # Test that date is unique
    entry = March(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert March.query.filter_by(date=2).first().date == 2
    entry = March.query.filter_by(date=2).first()
    entry.date = 1
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that headline can't be null
    entry = March.query.first()
    entry.headline = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that modtime can't be null
    entry = March.query.first()
    entry.modtime = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()

# April table test
def test_April(db_handle):

    # Test entry creation
    entry = April(link='https://www.google.com/', headline="First headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert April.query.count() == 1

    # Test getting an entry
    entry = April.query.filter_by(date=1).first()
    assert entry.headline == "First headline"

    # Test deletion of an entry
    entry = April(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert April.query.count() == 2
    entry = April.query.filter_by(date=2).first()
    db_handle.session.delete(entry)
    db_handle.session.commit()
    entry = April.query.first()
    assert entry.headline == "First headline"

    # Test modification of an entry
    entry = April.query.first()
    entry.headline = "New headline"
    db_handle.session.commit()
    entry = April.query.first()
    entry.headline = "New headline"

    # Test that date is unique
    entry = April(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert April.query.filter_by(date=2).first().date == 2
    entry = April.query.filter_by(date=2).first()
    entry.date = 1
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that headline can't be null
    entry = April.query.first()
    entry.headline = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that modtime can't be null
    entry = April.query.first()
    entry.modtime = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()

# May table test
def test_May(db_handle):

    # Test entry creation
    entry = May(link='https://www.google.com/', headline="First headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert May.query.count() == 1

    # Test getting an entry
    entry = May.query.filter_by(date=1).first()
    assert entry.headline == "First headline"

    # Test deletion of an entry
    entry = May(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert May.query.count() == 2
    entry = May.query.filter_by(date=2).first()
    db_handle.session.delete(entry)
    db_handle.session.commit()
    entry = May.query.first()
    assert entry.headline == "First headline"

    # Test modification of an entry
    entry = May.query.first()
    entry.headline = "New headline"
    db_handle.session.commit()
    entry = May.query.first()
    entry.headline = "New headline"

    # Test that date is unique
    entry = May(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert May.query.filter_by(date=2).first().date == 2
    entry = May.query.filter_by(date=2).first()
    entry.date = 1
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that headline can't be null
    entry = May.query.first()
    entry.headline = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that modtime can't be null
    entry = May.query.first()
    entry.modtime = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()

# June table test
def test_June(db_handle):

    # Test entry creation
    entry = June(link='https://www.google.com/', headline="First headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert June.query.count() == 1

    # Test getting an entry
    entry = June.query.filter_by(date=1).first()
    assert entry.headline == "First headline"

    # Test deletion of an entry
    entry = June(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert June.query.count() == 2
    entry = June.query.filter_by(date=2).first()
    db_handle.session.delete(entry)
    db_handle.session.commit()
    entry = June.query.first()
    assert entry.headline == "First headline"

    # Test modification of an entry
    entry = June.query.first()
    entry.headline = "New headline"
    db_handle.session.commit()
    entry = June.query.first()
    entry.headline = "New headline"

    # Test that date is unique
    entry = June(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert June.query.filter_by(date=2).first().date == 2
    entry = June.query.filter_by(date=2).first()
    entry.date = 1
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that headline can't be null
    entry = June.query.first()
    entry.headline = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that modtime can't be null
    entry = June.query.first()
    entry.modtime = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()

# July table test
def test_July(db_handle):

    # Test entry creation
    entry = July(link='https://www.google.com/', headline="First headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert July.query.count() == 1

    # Test getting an entry
    entry = July.query.filter_by(date=1).first()
    assert entry.headline == "First headline"

    # Test deletion of an entry
    entry = July(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert July.query.count() == 2
    entry = July.query.filter_by(date=2).first()
    db_handle.session.delete(entry)
    db_handle.session.commit()
    entry = July.query.first()
    assert entry.headline == "First headline"

    # Test modification of an entry
    entry = July.query.first()
    entry.headline = "New headline"
    db_handle.session.commit()
    entry = July.query.first()
    entry.headline = "New headline"

    # Test that date is unique
    entry = July(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert July.query.filter_by(date=2).first().date == 2
    entry = July.query.filter_by(date=2).first()
    entry.date = 1
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that headline can't be null
    entry = July.query.first()
    entry.headline = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that modtime can't be null
    entry = July.query.first()
    entry.modtime = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()

# August table test
def test_August(db_handle):

    # Test entry creation
    entry = August(link='https://www.google.com/', headline="First headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert August.query.count() == 1

    # Test getting an entry
    entry = August.query.filter_by(date=1).first()
    assert entry.headline == "First headline"

    # Test deletion of an entry
    entry = August(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert August.query.count() == 2
    entry = August.query.filter_by(date=2).first()
    db_handle.session.delete(entry)
    db_handle.session.commit()
    entry = August.query.first()
    assert entry.headline == "First headline"

    # Test modification of an entry
    entry = August.query.first()
    entry.headline = "New headline"
    db_handle.session.commit()
    entry = August.query.first()
    entry.headline = "New headline"

    # Test that date is unique
    entry = August(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert August.query.filter_by(date=2).first().date == 2
    entry = August.query.filter_by(date=2).first()
    entry.date = 1
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that headline can't be null
    entry = August.query.first()
    entry.headline = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that modtime can't be null
    entry = August.query.first()
    entry.modtime = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()

# September table test
def test_September(db_handle):

    # Test entry creation
    entry = September(link='https://www.google.com/', headline="First headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert September.query.count() == 1

    # Test getting an entry
    entry = September.query.filter_by(date=1).first()
    assert entry.headline == "First headline"

    # Test deletion of an entry
    entry = September(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert September.query.count() == 2
    entry = September.query.filter_by(date=2).first()
    db_handle.session.delete(entry)
    db_handle.session.commit()
    entry = September.query.first()
    assert entry.headline == "First headline"

    # Test modification of an entry
    entry = September.query.first()
    entry.headline = "New headline"
    db_handle.session.commit()
    entry = September.query.first()
    entry.headline = "New headline"

    # Test that date is unique
    entry = September(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert September.query.filter_by(date=2).first().date == 2
    entry = September.query.filter_by(date=2).first()
    entry.date = 1
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that headline can't be null
    entry = September.query.first()
    entry.headline = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that modtime can't be null
    entry = September.query.first()
    entry.modtime = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()

# October table test
def test_October(db_handle):

    # Test entry creation
    entry = October(link='https://www.google.com/', headline="First headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert October.query.count() == 1

    # Test getting an entry
    entry = October.query.filter_by(date=1).first()
    assert entry.headline == "First headline"

    # Test deletion of an entry
    entry = October(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert October.query.count() == 2
    entry = October.query.filter_by(date=2).first()
    db_handle.session.delete(entry)
    db_handle.session.commit()
    entry = October.query.first()
    assert entry.headline == "First headline"

    # Test modification of an entry
    entry = October.query.first()
    entry.headline = "New headline"
    db_handle.session.commit()
    entry = October.query.first()
    entry.headline = "New headline"

    # Test that date is unique
    entry = October(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert October.query.filter_by(date=2).first().date == 2
    entry = October.query.filter_by(date=2).first()
    entry.date = 1
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that headline can't be null
    entry = October.query.first()
    entry.headline = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that modtime can't be null
    entry = October.query.first()
    entry.modtime = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()

# November table test
def test_November(db_handle):

    # Test entry creation
    entry = November(link='https://www.google.com/', headline="First headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert November.query.count() == 1

    # Test getting an entry
    entry = November.query.filter_by(date=1).first()
    assert entry.headline == "First headline"

    # Test deletion of an entry
    entry = November(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert November.query.count() == 2
    entry = November.query.filter_by(date=2).first()
    db_handle.session.delete(entry)
    db_handle.session.commit()
    entry = November.query.first()
    assert entry.headline == "First headline"

    # Test modification of an entry
    entry = November.query.first()
    entry.headline = "New headline"
    db_handle.session.commit()
    entry = November.query.first()
    entry.headline = "New headline"

    # Test that date is unique
    entry = November(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert November.query.filter_by(date=2).first().date == 2
    entry = November.query.filter_by(date=2).first()
    entry.date = 1
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that headline can't be null
    entry = November.query.first()
    entry.headline = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that modtime can't be null
    entry = November.query.first()
    entry.modtime = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()

# December table test
def test_December(db_handle):

    # Test entry creation
    entry = December(link='https://www.google.com/', headline="First headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert December.query.count() == 1

    # Test getting an entry
    entry = December.query.filter_by(date=1).first()
    assert entry.headline == "First headline"

    # Test deletion of an entry
    entry = December(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert December.query.count() == 2
    entry = December.query.filter_by(date=2).first()
    db_handle.session.delete(entry)
    db_handle.session.commit()
    entry = December.query.first()
    assert entry.headline == "First headline"

    # Test modification of an entry
    entry = December.query.first()
    entry.headline = "New headline"
    db_handle.session.commit()
    entry = December.query.first()
    entry.headline = "New headline"

    # Test that date is unique
    entry = December(link='https://www.google.com/', headline="Second headline", modtime=datetime.now())
    db_handle.session.add(entry)
    db_handle.session.commit()
    assert December.query.filter_by(date=2).first().date == 2
    entry = December.query.filter_by(date=2).first()
    entry.date = 1
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that headline can't be null
    entry = December.query.first()
    entry.headline = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()
    db_handle.session.rollback()

    # Test that modtime can't be null
    entry = December.query.first()
    entry.modtime = None
    with pytest.raises(IntegrityError):
        db_handle.session.commit()