import pandas as pd
import requests
from pymongo import MongoClient
import pprint


def get_credentials():
    file = open("credentials.pass", "r")
    return {"username": file.readline().strip("\n"), "password": file.readline()}

creds = get_credentials()

print(creds)

client = MongoClient("mongodb://{0}:{1}@cluster0-shard-00-00-nwpjz.mongodb.net:27017,cluster0-shard-00-01-nwpjz.mongodb.net:27017,cluster0-shard-00-02-nwpjz.mongodb.net:27017/nhl?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority".format(creds["username"], creds["password"]))
db = client["nhl"]
collection = db["2019_2020"]

pprint.pprint(collection.find_one())


