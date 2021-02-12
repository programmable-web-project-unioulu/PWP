""" Simple SQLAlchemy model Programmable Web Course
Copyright: jjuutine20@student.oulu.fi, oanastoicescu11@gmail.com

An example from the exercise taken as a base and then modified (Measurement example)
"""

# BEGIN of the content taken from the exercise example
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# END of the content taken from the exercise example
# now group's own content from here on.

class Person(db.Model):
    """ Person- All columns required """
    id = db.Column(db.String(128), primary_key=True)

# Simple sanity check (ipython)
# In [1]: from app import db
# In [2]: db.create_all()
# In [3]: from app import Person
# In [4]: person = Person()
# In [5]: person.id = "123"
# In [9]: db.session.add(oatmeal)
# In [10]: db.session.commit()
# In [11]: print(person)
# <Person 123>

