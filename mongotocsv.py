import pymongo
import csv
import json

x=pymongo.MongoClient('mongodb://localhost:27017')
db=x['marvel']
col=db['avengers']

newdata=[]
for item in range (len(list(col.find()))):
    data={}
    for key in list(col.find())[item].keys():
        data[key]=list(col.find())[item][key]
    newdata.append(data)
print(newdata)

with open('mongo.csv','w',newline='') as x:
    writer=csv.DictWriter(x, fieldnames=newdata[0].keys())
    writer.writeheader()
    writer.writerows(newdata)