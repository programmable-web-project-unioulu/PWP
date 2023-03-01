from pymongo import MongoClient

DATABASE = MongoClient()["logbotdatabase"]
DEBUG = True
client = MongoClient('mongodb://128.214.254.176', 9005)