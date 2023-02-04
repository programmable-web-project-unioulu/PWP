from database import db, Group, Breed, Characteristics, Facts

def init_db():
    """
    this is an example of how to populate the database and
    create connections between them models
    """
    db.create_all()

    terrier_char = Characteristics(life_span="10 to 15 years", coat_length="3 inches", exercise="yes")
    terrier_facts = Facts(fact="They are awesome!")
    aus_terrier = Breed(name="Australian terrier", char=terrier_char, fact=terrier_facts)
    terrier_group = Group(name="Terriers", breed=aus_terrier)

    db.session.add(terrier_char)
    db.session.add(terrier_facts)
    db.session.add(aus_terrier)
    db.session.add(terrier_group)

    db.session.commit()

if __name__ == "__main__":
    init_db()
