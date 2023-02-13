## Tools Used

* MongoDB
* py-mongo (python library)

## Download MongoDB 
MongoDb can be downloaded from the official website for your relevant OS (Windows/mac/linux). Follow the instructions provided on the webpage for setting up mongodb on your local machine. Once installed, install py-mongo to be able to interact with mongoDB via a pythong script.
We recommend setting up a virtual environment so to ensure you have a self contained environment which will not affect your locally installed python packages

Setup a virtual environment

`python3 -m venv /path/to/venv/file`

Activate your virtual environment

`source activate /path/to/venv/file/bin/activate`

Install pymongo using pip install

`pip install pymongo`

## Create & Load Database

Run DataHandle.py in the db directory to create the collections in mongoDB

`python DataHandle.py`
