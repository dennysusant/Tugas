import pymongo
x=pymongo.MongoClient('mongodb://localhost:27017')
db=x['marvel']
col=db['avengers']

newdata=[]
for item in range (len(list(col.find()))):
    data={}
    for key in list(col.find())[item].keys():
        data[key]=str(list(col.find())[item][key])
    newdata.append(data)
with open('mongo.json','w') as x:
    x.write(str(newdata).replace("'",'"'))