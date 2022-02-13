# PWP SPRING 2022
# Movie Review
## Group information
* Samuel Knaus (samuel.knaus@student.oulu.fi)
* Marius Diamant (marius.diamant@etudiant.univ-rennes1.fr)
* Jonah Siedler (st150456@stud.uni-stuttgart.de)
* Jawad Akhtar (syedjawadakhtar@gmail.com)

## Setup
The dependencies are listed in the `MovieReview/backend/requirements.txt` file. If the noted libraries are not installed in your Python environment, install them using the following command: `pip install requirements.txt`.

We use Flask-SQLAlchemy in combination with SQLite3 to set up our database. The database design is given in `backend/database/database.py`. We use it in the `database_dummy_data.py` to set up an exemplary database. To test it, execute `python3 database_dummy_data.py`. The generated database can then be found as a file in the same folder (`movie-review.db`). There is no need to explicitly install SQLite since it is supported by Flask-SQLAlchemy natively.
