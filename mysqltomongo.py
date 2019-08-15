import mysql.connector
import pymongo
x=pymongo.MongoClient('mongodb://localhost:27017')

dbku = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='denny2310',
    auth_plugin = 'mysql_native_password'
)

kursor=dbku.cursor()
kursor.execute('use doraemon')
kursor.execute('describe karakter')
b=kursor.fetchall()
key=[]
val=[]
for item in b:
    key.append(item[0])
kursor.execute('use doraemon')
kursor.execute('select * from karakter')
a=kursor.fetchall()
for item in a:
    val.append(item)
isi=[]
for item in range(len(val)):
    new={}
    for item1 in range (len(val[item])):
        new[key[item1]]=val[item][item1]
    isi.append(new)


x=pymongo.MongoClient('mongodb://localhost:27017')

database=input('masukkan database: ')
db=x[str(database)]
collection=input('masukkan nama collection: ')
col=db[str(collection)]

for item in isi:
    col.insert_many(item)

