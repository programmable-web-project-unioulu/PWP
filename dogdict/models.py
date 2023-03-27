"""
    All db model definitions and a cli command for initialzing the db for testing
"""

from flask.cli import with_appcontext
import click
from dogdict import db


class Group(db.Model):
    """
        Group is an object that is used to categorize breeds. 
        Example: Australian Terrier belongs to the Terrier group of breeds.

        Each Group is unique and must have a name.
    """
    id = db.Column(db.Integer, primary_key=True)
    # must be unique
    name = db.Column(db.String(64), unique=True, nullable=False)

    # creates a connection from Group -> Breed
    breeds = db.relationship("Breed", back_populates="group")

    def serialize(self):
        """
            Used to serialize the Group Python model objects,
            since they can't directly be serialized with json.dumps
        """
        return {"name": self.name, "id": self.id}

    def deserialize(self, doc):
        """
            Used to deserialize the a dictionary into a suitable model instance.
        """
        self.name = doc["name"]

    @staticmethod
    def json_schema():
        """
            defines the JSON format of the Group object and describes the values
        """
        schema = {"type": "object", "required": ["name"]}
        props = schema["properties"] = {}
        props["name"] = {"description": "Group's unique name", "type": "string"}
        return schema


class Characteristics(db.Model):
    """
        Each characteristics can only have an 1 to 1 connection to a breed.
        This object characterises the breed and contains values such as
        life span, coat length and the amount of daily exercise the breed requires (in hours).

        There can be multiple similar characteristics, they are only separated by the ID.
    """
    id = db.Column(db.Integer, primary_key=True)
    life_span = db.Column(
        db.Integer,
        db.CheckConstraint("life_span>5"),
        db.CheckConstraint("life_span<25"),
        nullable=False,
    )
    coat_length = db.Column(
        db.Float, db.CheckConstraint("coat_length<1"), nullable=True
    )
    exercise = db.Column(
        db.Float,
        db.CheckConstraint("exercise>0"),
        db.CheckConstraint("exercise<5"),
        nullable=True,
    )

    # creates a connection between characteristics and breed
    in_breed = db.relationship("Breed", back_populates="characteristics")

    def serialize(self):
        """
            Used to serialize the Characteristics Python model objects,
            since they can't directly be serialized with json.dumps
        """
        return {
            "breed": [breed.name for breed in self.in_breed],
            "char_id": self.id,
            "coat_length": self.coat_length,
            "life_span": self.life_span,
            "exercise": self.exercise,
        }

    def deserialize(self, characteristic):
        """
            Used to deserialize the Characteristics objects to get specific
            characteristics from the DB (currently not required)
        """
        self.char = Characteristics.query.filter_by(name=characteristic["char_id"]).first()


    @staticmethod
    def json_schema():
        """
            defines the JSON format of the Characteristics object and describes the values
        """
        schema = {"type": "object", "required": ["in_breed", "life_span"]}
        props = schema["properties"] = {}
        props["in_breed"] = {
            "description": "Breed that the characteristics describe",
            "type": "string",
        }
        props["life_span"] = {"description": "Lifespan of a breed", "type": "number"}
        return schema


class Facts(db.Model):
    """
        Facts contain short information about breeds such as: "____ is a small dog"
        Facts can be non unique, but each fact can only belong to one breed.
    """
    id = db.Column(db.Integer, primary_key=True)
    fact = db.Column(db.String(128), nullable=False)

    # creates a connection from Facts -> Breed
    breed_id = db.Column(db.Integer, db.ForeignKey("breed.id", ondelete="CASCADE"))
    breed = db.relationship("Breed", back_populates="facts")

    def serialize(self):
        """
            Used to serialize the Facts Python model objects,
            since they can't directly be serialized with json.dumps
        """
        return {"fact": self.fact, "breed": self.breed_id, "id": self.id}

    def deserialize(self, doc):
        """
            Used to deserialize the Facts object and extract the wanted data
            Returns one specific fact currently
        """
        self.fact = doc["fact"]
        self.fact = Facts.query.filter_by(fact=doc["fact"]).first()


    @staticmethod
    def json_schema():
        """
            defines the JSON format of the Facts object and describes the values
        """
        schema = {"type": "object", "required": ["fact", "breed"]}
        props = schema["properties"] = {}
        props["fact"] = {"description": "Fact about a breed", "type": "string"}
        props["breed"] = {"description": "Breed regarding the fact", "type": "string"}
        return schema


class Breed(db.Model):
    """
        Each breed is unique and can only belong to one group.
        Each breed has characteristics that give information about the breeds. 1 to 1 Relationship.
        Each breed can have multiple facts.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    char_id = db.Column(
        db.Integer, db.ForeignKey("characteristics.id", ondelete="CASCADE")
    )

    # creates a connection from Breed -> Group
    group_id = db.Column(db.Integer, db.ForeignKey("group.id", ondelete="CASCADE"))
    group = db.relationship("Group", back_populates="breeds")

    # creates a connection from Breed -> Characteristics
    characteristics = db.relationship(
        "Characteristics", back_populates="in_breed", uselist=False
    )

    # creates a connection from Breed -> Facts
    facts = db.relationship("Facts", back_populates="breed")

    def serialize(self, short_form=False):
        """
            Used to serialize the Breed Python model objects,
            since they can't directly be serialized with json.dumps.
            
            Currently short_form doesn't affect anything.
        """
        doc = {"name": self.name, "id": self.id}
        if not short_form:
            doc["group"] = self.group.serialize()
            doc["facts"] = [fact.fact for fact in self.facts]
            if self.characteristics:
                doc["characteristics"] = {
                    "char_id": self.characteristics.id,
                    "life_span": self.characteristics.life_span,
                    "coat_length": self.characteristics.coat_length,
                    "exercise": self.characteristics.exercise,
                }
        print("this is breed.serialize", doc)
        return doc

    def deserialize(self, doc):
        """
            Used to deserialize the a dictionary into a suitable model instance.
        """
        self.name = doc["name"]
        if not doc["group"]:
            return
        self.group = Group.query.filter_by(name=doc["group"]).first()

    @staticmethod
    def json_schema():
        """
            defines the JSON format of the Breed object and describes the values
        """
        schema = {"type": "object", "required": ["name", "group"]}
        props = schema["properties"] = {}
        props["name"] = {"description": "Breeds unique name", "type": "string"}
        props["group"] = {"description": "Name of the breed's group", "type": "string"}
        return schema


@click.command("init-db")
@with_appcontext
def init_db():
    """
        Command line interface to initiliaze a test db to instances/test.db
    """
    db.create_all()
    terriergroup = Group(name="Terrier")
    pastoralgroup = Group(name="Pastoral")
    workinggroup = Group(name="Working")

    # Create a new characteristics
    characteristics_at = Characteristics(life_span=6, coat_length=0.2, exercise=1.2)
    characteristics_asd = Characteristics(life_span=7, coat_length=0.3, exercise=3.3)
    characteristics_am = Characteristics(life_span=8, coat_length=0.4, exercise=3.5)
    characteristics_as = Characteristics(life_span=9, coat_length=0.99, exercise=4.75)

    # Create a new breed and associate it with the group and characteristics
    breed_at = Breed(
        name="Australian Terrier",
        group=terriergroup,
        characteristics=characteristics_at,
    )
    breed_asd = Breed(
        name="Anatolina Shepherd Dog",
        group=pastoralgroup,
        characteristics=characteristics_asd,
    )
    breed_am = Breed(
        name="Alaskan malamute", group=workinggroup, characteristics=characteristics_am
    )
    breed_as = Breed(
        name="Australian Shepherd",
        group=pastoralgroup,
        characteristics=characteristics_as,
    )

    # Create two facts and associate them with the breed
    fact1 = Facts(fact="Välillä kuin (australian) terrieri...", breed=breed_at)
    fact2 = Facts(fact="They are small dogs", breed=breed_at)

    fact_asd = Facts(
        fact="They have history as livestock guardians and they bark alot",
        breed=breed_asd,
    )
    fact_am = Facts(
        fact="""An immensely strong, heavy-duty worker of spitz type
        , the Alaskan Malamute is an affectionate, loyal, and playful dog""",
        breed=breed_am,
    )

    # Repeat the above for another breed
    breed2 = Breed(
        name="Laurin Terrier", group=terriergroup, characteristics=characteristics_at
    )

    fact3 = Facts(fact="Välillä kuin (australian) terrieri...", breed=breed2)
    fact4 = Facts(fact="They are small dogs", breed=breed2)

    # Commit the changes to the database
    db.session.add(terriergroup)
    db.session.add(pastoralgroup)
    db.session.add(workinggroup)

    db.session.add(characteristics_at)
    db.session.add(characteristics_asd)
    db.session.add(characteristics_am)
    db.session.add(characteristics_as)

    db.session.add(breed_at)
    db.session.add(breed_as)
    db.session.add(fact1)
    db.session.add(fact2)
    db.session.add(fact_asd)
    db.session.add(fact_am)

    db.session.add(breed2)
    db.session.add(fact3)
    db.session.add(fact4)

    db.session.commit()
