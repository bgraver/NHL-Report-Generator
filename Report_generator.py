import pandas as pd
import requests
from pymongo import MongoClient
import pprint


# client = MongoClient("mongodb+srv://bgraver:UAAfK3eTaRqiqCV@cluster0-nwpjz.mongodb.net/?retryWrites=true&w=majority", 27017)
client = MongoClient("mongodb://bgrave3:BcKvxdBh6M3gzKr@cluster0-shard-00-00-nwpjz.mongodb.net:27017,cluster0-shard-00-01-nwpjz.mongodb.net:27017,cluster0-shard-00-02-nwpjz.mongodb.net:27017/nhl?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client["nhl"]
collection = db["2019_2020"]

pprint.pprint(collection.find_one())



