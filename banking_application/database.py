from os import environ as env
from pymongo import MongoClient


def connect():
    """ Connect to MongoDB using srv string (which is stored as an environmental variable). """
    return MongoClient(env.get("MONGODB_CONNECTION_STRING"))

