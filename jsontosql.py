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
with open('convert.json') as x:
    data=json.load(x)
key=[]
for item in data[0].keys():
    key.append(item)
print(key)
dbs=input('masukkan nama database baru: ')
tabel=input('masukkan nama tabel: ')
kursor=dbku.cursor()
kursor.execute('create database {}'.format(dbs))
kursor.execute('use {}'.format(dbs))
querydb='''create table {}(
    tes int)
   '''.format(tabel)
kursor.execute(querydb)
for item1 in key:
    querydb='''alter table {}
    add column
    {}
    ;
    '''.format(tabel,item1.replace(' ','')+' '+'varchar(100)')
    kursor.execute(querydb)
querydb='''alter table {}
drop column tes'''.format(tabel)
kursor.execute(querydb)


for item in (data):
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
    querydb='''insert into {} {} values
    {}
    '''.format(tabel,c,b)
    kursor.execute(querydb)
    

dbku.commit()