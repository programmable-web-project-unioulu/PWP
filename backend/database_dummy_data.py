import database
from database import Category, Movie, Review, User, UserType
import datetime

db = database.db

# set up the environment
db.create_all()
db.session.rollback()

# create the dummy user
user_1 = User(
    username="dummyGuy",
    emailAddress="red.unicorn@gmail.com",
    password="thisisnotapassword",
    role=UserType.basicUser
)

user_2 = User(
    username="dummyAdmin",
    emailAddress="omnipotent.pencil@yahoo.com",
    password="1234",
    role=UserType.admin
)

user_3 = User(
    username="grantorinohurricane",
    emailAddress="grantorinohurricane@gmail.com",
    password="Grantorino1234",
    role=UserType.basicUser
)

user_4 = User(
    username="lightningbasketball",
    emailAddress="lightningbasketbal@gmail.com",
    password="Basketball1234",
    role=UserType.basicUser
)

user_5 = User(
    username="johnkennedy",
    emailAddress="kennedyj@moviereview.com",
    password="$KenJon9908",
    role=UserType.admin
)

db.session.add(user_1)
db.session.add(user_2)
db.session.add(user_3)
db.session.add(user_4)
db.session.add(user_5)
db.session.commit()

# create the categories
category_1 = Category(
    title="Thriller"
)

category_2 = Category(
    title="War"
)

category_3 = Category(
    title="Adventure"
)

category_4 = Category(
    title="Animation"
)

category_5 = Category(
    title="Action"
)

db.session.add(category_1)
db.session.add(category_2)
db.session.add(category_3)
db.session.add(category_4)
db.session.add(category_5)
db.session.commit()

# create the movies
movie_1 = Movie(
    title="Léon: The professional",
    director="Luc Besson",
    length=110,
    release_date=datetime.datetime(1999, 9, 14),
    category_id=category_1.id
)

movie_2 = Movie(
    title="Apocalypse Now",
    director="Francis Coppola",
    length=123,
    release_date=datetime.datetime(1997, 8, 15),
    category_id=category_2.id
)

movie_3 = Movie(
    title="Spider-Man: No Way Home",
    director="Jon Watts",
    length=148,
    release_date=datetime.datetime(2021, 12, 13),
    category_id=category_3.id
)

movie_4 = Movie(
    title="Frozen",
    director="Chris Buck",
    length=102,
    release_date=datetime.datetime(2013, 11, 19),
    category_id=category_4.id
)

movie_5 = Movie(
    title="Red Notice",
    director="Rawson Marshall Thurber",
    length=118,
    release_date=datetime.datetime(2021, 11, 5),
    category_id=category_5.id
)

db.session.add(movie_1)
db.session.add(movie_2)
db.session.add(movie_3)
db.session.add(movie_4)
db.session.add(movie_5)
db.session.commit()

# create the reviews
review_1 = Review(
    rating=4,
    comment="The film is almost perfect but I don’t like Natalie Portman",
    date=datetime.datetime(2016, 9, 10),
    author_id=user_1.id,
    movie_id=movie_1.id
)

review_2 = Review(
    rating=5,
    comment="Such a masterpiece! I love helicopters",
    date=datetime.datetime(2018, 5, 23),
    author_id=user_1.id,
    movie_id=movie_2.id
)

review_3 = Review(
    rating=5,
    comment="Amazing movie! This movie was amazing! Both me and my kids loved it! There is a little more brutal action than the other movies so be prepared for that.",
    date=datetime.datetime(2021, 12, 20),
    author_id=user_3.id,
    movie_id=movie_3.id
)

review_4 = Review(
    rating=4,
    comment="Will melt the iciest of hearts, the best animated film of 2013 by a mile and one of Disney's best in recent years.",
    date=datetime.datetime(2014, 3, 15),
    author_id=user_3.id,
    movie_id=movie_4.id
)

review_5 = Review(
    rating=5,
    comment="My girls totally love it! Been watching with them every weekend now (seems boring now), yet my kids every time feel rejuvenated after watching it.",
    date=datetime.datetime(2015, 5, 31),
    author_id=user_4.id,
    movie_id=movie_4.id
)

review_6 = Review(
    rating=2,
    comment="Not as good as I was anticipating. A few good jokes and fight scenes, but the script was bland and the visuals looked fake. An all-star cast but no substance to the story or characters.",
    date=datetime.datetime(2021, 12, 1),
    author_id=user_5.id,
    movie_id=movie_5.id
)

db.session.add(review_1)
db.session.add(review_2)
db.session.add(review_3)
db.session.add(review_4)
db.session.add(review_5)
db.session.add(review_6)

db.session.commit()
