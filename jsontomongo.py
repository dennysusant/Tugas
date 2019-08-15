import pymongo
import csv
import json

x=pymongo.MongoClient('mongodb://localhost:27017')

database=input('masukkan database: ')
db=x[str(database)]
collection=input('masukkan nama collection: ')
col=db[str(collection)]

with open('mongo.json') as k:
    data=json.load(k)
for item in data:
    col.insert(data)
