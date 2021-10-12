import csv
import os
import pandas as pd
import json
from pymongo import MongoClient

HOST = 'cluster0.mcod1.mongodb.net'
USER = 'yangyanguser'
PASSWORD = 'yangyang1234'
DATABASE_NAME = 'myFirstDatabase'
COLLECTION_NAME = 'flight_fare'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

data = json.loads(pd.read_excel('data/Data_Train.xlsx').to_json(orient='records'))
coll = MongoClient(MONGO_URI)[DATABASE_NAME][COLLECTION_NAME]
coll.insert_many(data) 