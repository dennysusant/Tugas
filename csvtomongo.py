import json
import csv
import pymongo

x=pymongo.MongoClient('mongodb://localhost:27017')

database=input('masukkan database: ')
db=x[str(database)]
collection=input('masukkan nama collection: ')
col=db[str(collection)]


file = open ('mongo.csv','r')
json1=[]
with open('mongo.csv','r') as x:
    reader=csv.DictReader(x)
    for i in reader:
        json1.append(dict(i))
print(json1)
for item in json1:
    col.insert (item)


