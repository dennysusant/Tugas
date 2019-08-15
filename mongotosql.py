import pymongo
import mysql.connector
import csv
import json
dbku = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='denny2310',
    auth_plugin = 'mysql_native_password'
)


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

 

kursor=dbku.cursor()
kursor.execute('create database frommongo')
kursor.execute('use frommongo')
querydb='''create table mongo(
    tes int)
   '''
kursor.execute(querydb)
for item1 in newdata[0].keys():
    querydb='''alter table mongo
    add column
    {}
    ;
    '''.format(item1.replace(' ','')+' '+'varchar(100)')
    kursor.execute(querydb)
querydb='''alter table mongo
drop column tes'''
kursor.execute(querydb)



for item in (newdata):
    c=[]
    b=[]
    for item1 in list(item.keys()):
        c.append(item1)
        b.append(str(item[item1]))
    c=str(c)
    b=str(b)
    c=c.replace('[','(')
    c=c.replace("'","")
    c=c.replace(']',')')
    c=c.replace(' ','')
    b=b.replace('[','(')
    b=b.replace(']',')')
    querydb='''insert into mongo {} values
    {}
    '''.format(c,b)
    kursor.execute(querydb)
    

dbku.commit()