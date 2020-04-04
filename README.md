# PWP SPRING 2020
# Florida Man Generator
# Group information
* Student 1. Aleksi Hytönen, hytonenaleksi@gmail.com
* Student 2. Markus Oja, markus.oja@student.oulu.fi

__Remember to include all required documentation and HOWTOs, including how to create and populate the database, how to run and test the API, the url to the entrypoint and instructions on how to setup and run the client__

# Overview of the API
## Structure
### db <Database>
db_test.py = Unit tests for the database.<br>
db.py = Database models.<br>
populate.py = Populate the database with initial values.<br>
README.md = Instructions on how to use the database.<br>
test.db = Populated database with initial values.
### src <Source Code>
#### builders <Builders for all resources>
addedarticlebuilder.py = Builder for added article resource.<br>
articlebuilder.py = Builder for article resource.<br>
masonbuilder.py = Builder to create resources. Used in other builders as dependency.<br>
userbuilder.py = Builder for user resource.
#### Resources <The actual resources of the API>
addedarticleresource.py = Resource for added article collection and item.<br>
articleresource.py = Resource for article collection and item.<br>
entrypoint.py = Application entrypoint.<br>
userresource.py = Resource for user collection and item.
## Usage
1. Install dependencies
```shell
pip install -r requirements.txt
```
2. start the API
```shell
flask run
```
## Test the API

# apitest:

This empties the database...

Run apitest with pytest in the root folder
(no need for flask to run (not at the moment at least))
```shell
pytest apitest.py
```

