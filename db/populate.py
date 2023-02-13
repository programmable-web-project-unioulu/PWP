from database import db, Group, Breed, Characteristics, Facts
import os

def init_db():
    """
    this is an example of how to populate the database and
    create connections between them models
    """

    db.create_all()


    terriergroup = Group(name="Terrier")
    pastoralgroup = Group(name="Pastoral")
    workinggroup = Group(name="Working")
    

    # Create a new characteristics
    characteristics_at = Characteristics(life_span="10 years", coat_length="long", exercise="daily")
    characteristics_asd = Characteristics(life_span="over 10 years", coat_length="short", exercise="more than two hours a day")
    characteristics_am = Characteristics(life_span="over 10 years", coat_length="medium", exercise="more than two hours a day")
    characteristics_as = Characteristics(life_span="over 10 years", coat_length="medium", exercise="more than two hours a day")

    # Create a new breed and associate it with the group and characteristics
    breed_at = Breed(name="Australian Terrier", group=terriergroup, characteristics=characteristics_at)
    breed_asd = Breed(name="Anatolina Shepherd Dog", group=pastoralgroup, characteristics=characteristics_asd)
    breed_am = Breed(name="Alaskan malamute", group=workinggroup, characteristics=characteristics_am)
    breed_as = Breed(name="Australian Shepherd", group=pastoralgroup, characteristics=characteristics_as)


    # Create two facts and associate them with the breed
    fact1 = Facts(fact="Välillä kuin (australian) terrieri...", breed=breed_at)
    fact2 = Facts(fact="They are small dogs", breed=breed_at)

    fact_asd = Facts(fact="They have history as livestock guardians and they bark alot", breed=breed_asd)
    fact_am = Facts(fact="An immensely strong, heavy-duty worker of spitz type, the Alaskan Malamute is an affectionate, loyal, and playful dog", breed=breed_am)

    # Repeat the above for another breed
    breed2 = Breed(name="Laurin Terrier", group=terriergroup, characteristics=characteristics_at)

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

if __name__ == "__main__":
    init_db()