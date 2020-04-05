# Database implementation (DL 2)

## Dependencies
All dependencies can be found from requirements.txt.

### Installing dependencies
1. Activate python virtual environment in command line
```shell
virtualenv pwp
```
2. Activate virtual environment
```shell
pwp\Scripts\activate.bat
```
3. install dependencies
```shell
pip install -r requirements.txt
```

## Definition
The database is implemented using SQLite. It contains 12 tables, one for each month.

You can find visual representation of the tables from [wiki](https://github.com/Svenskapojkarna/Florida-Man-Generator/wiki/Database-design-and-implementation).
Models can be found at db.py.

## Setup and populate the database
In python virtual environment (instructions above), run command:
```shell
python populate.py
```
This script will create and populate the database.

There will be a new entry for each day of the year.


