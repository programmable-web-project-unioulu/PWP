# PWP 2020
# PlantDiery
# Group information
* Laura Punkeri
* Nuutti Räihä

__Remember to include all required documentation and HOWTOs, including how to create and populate the database, how to run and test the API, the url to the entrypoint and instructions on how to setup and run the client__
-jeeejee


# How-to when WIP

Works with python3.7. 
Python3.9 does not work.
 
## Virtualenv

```
pip3 install virtualenv
```


```
virtualenv venv
```


```
source venv/bin/activate

```

```
pip3 install -r requirements.txt
```

```
export FLASK_ENV=development
export FLASK_APP=PlantDiery
flask init-db
flask run
```
