# PWP SPRING 2023
# DogDict API
![CircleCI](https://dl.circleci.com/status-badge/img/gh/mmouru/pwp-RESTful-api/tree/master.svg?style=shield)
# Group information
* Student 1. Martti Mourujärvi   mmouruja19@student.oulu.fi
* Student 2. Kalle Veijalainen   kveijala19@student.oulu.fi
* Student 3. Juho Kurula         jkurula19@student.oulu.fi
* Student 4. Lauri Suutari       lsuutari19@student.oulu.fi

__Remember to include all required documentation and HOWTOs, including how to create and populate the database, how to run and test the API, the url to the entrypoint and instructions on how to setup and run the client__

### Database instructions
All dependencies are listed in [requirements.txt](https://github.com/mmouru/pwp-RESTful-api/blob/master/requirements.txt). Database is created with [Flask](https://pypi.org/project/Flask/2.1.3/) (version 2.1.3) and [Flask-SQLAlchemy](https://pypi.org/project/Flask-SQLAlchemy/2.5.1/) (version 2.5.1). 

To install required external libraries and dependencies, use the following command:

```
cd pwp-RESTful-api
pip install -r requirements.txt
```

The repository contains an example on how to create and populate the database defined in [database.py](https://github.com/mmouru/pwp-RESTful-api/blob/master/db/database.py).

NOTE: Please make sure you do not already have an existing [test.db](https://github.com/mmouru/pwp-RESTful-api/blob/master/db/instance/test.db) file. It needs to be removed before creating a new one.

To create and populate the database, use the following command:
```
cd db
python populate.py
```

After creating the database it can be found at location:
```
cd instance
```

To view the contents of the database, a VSCode extension such as [SQLite Viewer](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer) can be used.

## Testing

Models are tested using pytest with coverage reports. Currently could only get coverage report to work for
singular files, e.g. for database.py only.

*TODO*
- Better folder structure
- Find good parameters to call pytest to get full coverage report
- Get 100% test coverage

How to get coverage % for separate files:
-v flag is for verbose
add -vv for more information in testing if needed
```
python -m pytest --cov=api -v
python -m pytest --cov=database -v

```

## Running with docker
You can build and run the app using docker for easier integration.
Build in root directory where Dockerfile is present
When running you can specify networking inside container so that the app is available in your machine, here port 3000.
```
docker build . --tag dogdict-app
docker run -p 3000:5000 dogdict-app
```
