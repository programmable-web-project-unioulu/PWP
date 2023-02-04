from database import db, Group, Breed, Characteristics, Facts
import os

def init_db():
    """
    this is an example of how to populate the database and
    create connections between them models
    """

    db.create_all()


    group = Group(name="Terrier")

    # Create a new characteristics
    characteristics = Characteristics(life_span="10 years", coat_length="long", exercise="daily")

    # Create a new breed and associate it with the group and characteristics
    breed1 = Breed(name="Australian Terrier", group=group, characteristics=characteristics)

    # Create two facts and associate them with the breed
    fact1 = Facts(fact="Välillä kuin (australian) terrieri...", breed=breed1)
    fact2 = Facts(fact="They are small dogs", breed=breed1)

    # Repeat the above for another breed
    breed2 = Breed(name="Laurin Terrier", group=group, characteristics=characteristics)

    fact3 = Facts(fact="Välillä kuin (australian) terrieri...", breed=breed2)
    fact4 = Facts(fact="They are small dogs", breed=breed2)

    # Commit the changes to the database
    db.session.add(group)
    db.session.add(characteristics)
    db.session.add(breed1)
    db.session.add(fact1)
    db.session.add(fact2)

    db.session.add(breed2)
    db.session.add(fact3)
    db.session.add(fact4)

    db.session.commit()

if __name__ == "__main__":
    init_db()